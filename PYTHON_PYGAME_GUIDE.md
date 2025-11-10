# 🐍 Shade & Source - Python + Pygame Implementation Guide

## 🎯 Technology Stack: Python 3.11+ with Pygame

This document provides Python/Pygame-specific implementation guidance for the Level 1 MVP prototype.

---

## 📦 Project Setup

### Required Dependencies

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install pygame==2.5.2
pip install numpy==1.24.3  # For shadow projection calculations
```

### Project Structure

```
puzzle-game/
├── docs/                          # Existing documentation (DO NOT MODIFY)
├── game/                          # Python implementation (CREATE THIS)
│   ├── main.py                    # Entry point
│   ├── config.py                  # Constants and configuration
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── source.py              # Source character class
│   │   ├── shade.py               # Shade (shadow) class
│   │   └── light_source.py        # Light source class
│   ├── mechanics/
│   │   ├── __init__.py
│   │   ├── shadow_projection.py   # Shadow calculation system
│   │   ├── death_detection.py     # Death/collision detection
│   │   └── laser_gate.py          # Laser gate + bridge mechanics
│   ├── level.py                   # Level 1 implementation
│   ├── game_manager.py            # Main game loop and state
│   └── ui.py                      # UI elements (timer, death counter)
├── assets/                        # (optional - using geometric shapes)
├── requirements.txt
├── README_IMPLEMENTATION.md
└── .gitignore
```

---

## 🎨 Pygame Implementation Specifics

### Window Setup (config.py)

```python
import pygame

# Window configuration
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FPS = 60

# Game grid (from documentation)
GRID_UNIT_SIZE = 32  # pixels per unit
GRID_WIDTH = 30      # units
GRID_HEIGHT = 20     # units
GAME_WIDTH = GRID_WIDTH * GRID_UNIT_SIZE   # 960 pixels
GAME_HEIGHT = GRID_HEIGHT * GRID_UNIT_SIZE  # 640 pixels

# Scale factor for display (960x640 → 1920x1080)
SCALE_FACTOR = min(WINDOW_WIDTH / GAME_WIDTH, WINDOW_HEIGHT / GAME_HEIGHT)

# Color palette (exact hex codes from documentation)
COLOR_BACKGROUND = (26, 26, 26)      # #1A1A1A
COLOR_LIGHT_ZONE = (245, 245, 245)   # #F5F5F5
COLOR_SHADOW_ZONE = (13, 13, 13)     # #0D0D0D
COLOR_PLATFORM = (128, 128, 128)     # #808080
COLOR_SOURCE_GLOW = (255, 229, 204)  # #FFE5CC (5% opacity)
COLOR_SHADE_GLOW = (204, 229, 255)   # #CCE5FF (3% opacity)
COLOR_GOAL = (204, 255, 229)         # #CCFFE5
COLOR_LASER = (255, 102, 102)        # #FF6666
```

### Main Game Loop (main.py)

```python
import pygame
import sys
from config import *
from game_manager import GameManager

def main():
    pygame.init()
    
    # Create window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Shade & Source - Level 1: The Basic Divide")
    
    # Create game surface (internal resolution)
    game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    
    # Clock for FPS
    clock = pygame.time.Clock()
    
    # Game manager
    game_manager = GameManager()
    
    # Main loop
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_manager.handle_event(event)
        
        # Update
        game_manager.update(dt)
        
        # Render to game surface
        game_surface.fill(COLOR_BACKGROUND)
        game_manager.render(game_surface)
        
        # Scale and blit to screen
        scaled_surface = pygame.transform.scale(
            game_surface,
            (int(GAME_WIDTH * SCALE_FACTOR), int(GAME_HEIGHT * SCALE_FACTOR))
        )
        screen.fill((0, 0, 0))
        offset_x = (WINDOW_WIDTH - scaled_surface.get_width()) // 2
        offset_y = (WINDOW_HEIGHT - scaled_surface.get_height()) // 2
        screen.blit(scaled_surface, (offset_x, offset_y))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```

---

## 🎮 Core Systems Implementation

### Shadow Projection (mechanics/shadow_projection.py)

```python
import numpy as np
from config import GRID_UNIT_SIZE

class ShadowProjector:
    """
    Calculates shadow position based on Source position and Light position.
    
    Formula from MECHANICS_DEEP_DIVE.md:
    Shadow Position = Source Pos + (Source Pos - Light Pos) × Extension Factor
    Extension Factor = (Shadow Plane Y - Light Y) / (Source Y - Light Y)
    """
    
    @staticmethod
    def calculate_shade_position(source_pos, light_pos, shadow_plane_y):
        """
        Args:
            source_pos: (x, y) tuple in grid units
            light_pos: (x, y) tuple in grid units
            shadow_plane_y: Y coordinate of shadow floor in grid units
        
        Returns:
            (x, y) tuple for Shade position in grid units
        """
        sx, sy = source_pos
        lx, ly = light_pos
        
        # Vector from light to source
        dx = sx - lx
        dy = sy - ly
        
        # Prevent division by zero
        if abs(dy) < 0.01:
            # Source is at same Y as light - shadow projects to infinity
            # Return a position off-screen (this is a death condition)
            return (sx + 1000, shadow_plane_y)
        
        # Calculate extension factor
        t = (shadow_plane_y - ly) / dy
        
        # Shade position
        shade_x = lx + (dx * t)
        shade_y = shadow_plane_y
        
        return (shade_x, shade_y)
    
    @staticmethod
    def is_in_light_radius(entity_pos, light_pos, light_radius):
        """
        Check if entity is within light radius.
        
        Args:
            entity_pos: (x, y) tuple in grid units
            light_pos: (x, y) tuple in grid units
            light_radius: Radius in grid units
        
        Returns:
            True if entity is in light, False otherwise
        """
        distance = np.sqrt(
            (entity_pos[0] - light_pos[0])**2 +
            (entity_pos[1] - light_pos[1])**2
        )
        return distance <= light_radius
```

### Source Character (entities/source.py)

```python
import pygame
from config import *

class Source:
    """
    The Source character - player-controlled entity.
    Must stay in light to survive.
    """
    
    def __init__(self, start_x, start_y):
        # Position in grid units
        self.x = start_x
        self.y = start_y
        self.start_x = start_x
        self.start_y = start_y
        
        # Size (from documentation: 10 units wide, 20 units tall)
        self.width = 0.31  # grid units (10 pixels / 32)
        self.height = 0.625  # grid units (20 pixels / 32)
        
        # Physics
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 4.0  # units per second
        self.jump_force = -10.0  # upward velocity
        self.gravity = 20.0  # units per second^2
        self.on_ground = False
        
        # State
        self.alive = True
    
    def handle_input(self, keys):
        """Handle keyboard input."""
        # Horizontal movement
        self.velocity_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity_x = self.speed
        
        # Jump
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.on_ground:
            self.velocity_y = self.jump_force
            self.on_ground = False
    
    def update(self, dt, platforms):
        """Update position and physics."""
        if not self.alive:
            return
        
        # Apply gravity
        self.velocity_y += self.gravity * dt
        
        # Update position
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        
        # Platform collision (simple AABB)
        self.on_ground = False
        for platform in platforms:
            if self.check_collision(platform):
                # Simple collision response (push up)
                self.y = platform['y'] - self.height
                self.velocity_y = 0
                self.on_ground = True
    
    def check_collision(self, platform):
        """Check AABB collision with platform."""
        return (self.x < platform['x'] + platform['width'] and
                self.x + self.width > platform['x'] and
                self.y < platform['y'] + platform['height'] and
                self.y + self.height > platform['y'])
    
    def render(self, surface):
        """Render Source character."""
        # Convert grid units to pixels
        pixel_x = int(self.x * GRID_UNIT_SIZE)
        pixel_y = int(self.y * GRID_UNIT_SIZE)
        pixel_w = int(self.width * GRID_UNIT_SIZE)
        pixel_h = int(self.height * GRID_UNIT_SIZE)
        
        # Draw geometric humanoid (simplified for MVP)
        # Head (circle)
        head_radius = pixel_w // 2
        head_center = (pixel_x + pixel_w // 2, pixel_y + head_radius)
        pygame.draw.circle(surface, (255, 255, 255), head_center, head_radius)
        
        # Body (rectangle)
        body_rect = pygame.Rect(
            pixel_x + pixel_w // 4,
            pixel_y + head_radius * 2,
            pixel_w // 2,
            pixel_h - head_radius * 2
        )
        pygame.draw.rect(surface, (255, 255, 255), body_rect)
        
        # Glow effect (optional - 5% opacity)
        glow_surface = pygame.Surface((pixel_w + 10, pixel_h + 10), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (*COLOR_SOURCE_GLOW, 13), 
                         (pixel_w // 2 + 5, pixel_h // 2 + 5), 
                         max(pixel_w, pixel_h) // 2 + 5)
        surface.blit(glow_surface, (pixel_x - 5, pixel_y - 5))
    
    def reset(self):
        """Reset to start position."""
        self.x = self.start_x
        self.y = self.start_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.alive = True
```

---

## 🔧 Level 1 Implementation (level.py)

```python
import pygame
from config import *
from entities.source import Source
from entities.shade import Shade
from entities.light_source import LightSource
from mechanics.shadow_projection import ShadowProjector
from mechanics.laser_gate import LaserGate

class Level1:
    """
    Level 1: The Basic Divide
    
    Layout from LEVEL_1_IMPLEMENTATION.md with exact coordinates.
    """
    
    def __init__(self):
        # Platforms (from documentation)
        self.platforms = [
            {'x': 0, 'y': 3, 'width': 30, 'height': 2},   # Ground
            {'x': 0, 'y': 7, 'width': 14, 'height': 2},   # Mid left
            {'x': 20, 'y': 7, 'width': 10, 'height': 2},  # Mid right
            {'x': 0, 'y': 11, 'width': 30, 'height': 2},  # Top
        ]
        
        # Shadow floor (for Shade only)
        self.shadow_floor = {'x': 0, 'y': -2, 'width': 30, 'height': 2}
        
        # Entities
        self.source = Source(6, 5)  # Start position from docs
        self.light = LightSource(15, 18, 12)  # Position, radius from docs
        self.shade = Shade(self.shadow_floor['y'])
        
        # Mechanics
        self.projector = ShadowProjector()
        self.laser_gate = LaserGate(12, -5, 6, 8)  # Position, size from docs
        
        # Bridge (spawned by laser gate)
        self.bridge = None
        self.bridge_active = False
        
        # Goal
        self.goal = {'x': 18, 'y': 12, 'width': 3, 'height': 3}
        
        # Game state
        self.deaths = 0
        self.start_time = pygame.time.get_ticks()
        self.completed = False
    
    def update(self, dt):
        """Update level state."""
        # Update Source
        keys = pygame.key.get_pressed()
        self.source.handle_input(keys)
        self.source.update(dt, self.platforms + ([self.bridge] if self.bridge_active else []))
        
        # Calculate Shade position
        shade_pos = self.projector.calculate_shade_position(
            (self.source.x, self.source.y),
            (self.light.x, self.light.y),
            self.shadow_floor['y']
        )
        self.shade.update(shade_pos)
        
        # Check death conditions
        self.check_death()
        
        # Update laser gate
        if self.laser_gate.check_shade_collision(self.shade):
            if not self.bridge_active:
                self.spawn_bridge()
        
        # Check win condition
        self.check_win()
    
    def check_death(self):
        """Check if Source or Shade died."""
        # Source must be in light
        source_in_light = self.projector.is_in_light_radius(
            (self.source.x, self.source.y),
            (self.light.x, self.light.y),
            self.light.radius
        )
        
        if not source_in_light:
            self.death_reset("Source entered shadow")
            return
        
        # Shade must be in darkness (not in light)
        shade_in_light = self.projector.is_in_light_radius(
            (self.shade.x, self.shade.y),
            (self.light.x, self.light.y),
            self.light.radius
        )
        
        if shade_in_light:
            self.death_reset("Shade entered light")
            return
    
    def death_reset(self, reason):
        """Reset level after death."""
        print(f"Death: {reason}")
        self.deaths += 1
        self.source.reset()
        self.bridge_active = False
        self.bridge = None
    
    def spawn_bridge(self):
        """Spawn bridge across gap."""
        self.bridge = {'x': 14, 'y': 7, 'width': 6, 'height': 2}
        self.bridge_active = True
        print("Bridge spawned!")
    
    def check_win(self):
        """Check if Source reached goal."""
        if self.source.check_collision(self.goal):
            self.completed = True
            elapsed = (pygame.time.get_ticks() - self.start_time) / 1000.0
            print(f"Level Complete! Time: {elapsed:.1f}s, Deaths: {self.deaths}")
    
    def render(self, surface):
        """Render level."""
        # Platforms
        for platform in self.platforms:
            rect = pygame.Rect(
                platform['x'] * GRID_UNIT_SIZE,
                platform['y'] * GRID_UNIT_SIZE,
                platform['width'] * GRID_UNIT_SIZE,
                platform['height'] * GRID_UNIT_SIZE
            )
            pygame.draw.rect(surface, COLOR_PLATFORM, rect)
        
        # Bridge (if active)
        if self.bridge_active and self.bridge:
            rect = pygame.Rect(
                self.bridge['x'] * GRID_UNIT_SIZE,
                self.bridge['y'] * GRID_UNIT_SIZE,
                self.bridge['width'] * GRID_UNIT_SIZE,
                self.bridge['height'] * GRID_UNIT_SIZE
            )
            pygame.draw.rect(surface, (160, 160, 160), rect)  # Lighter grey
        
        # Light source
        self.light.render(surface)
        
        # Shadow floor (visual reference)
        shadow_rect = pygame.Rect(
            self.shadow_floor['x'] * GRID_UNIT_SIZE,
            (self.shadow_floor['y'] + GRID_HEIGHT) * GRID_UNIT_SIZE,  # Offset for display
            self.shadow_floor['width'] * GRID_UNIT_SIZE,
            self.shadow_floor['height'] * GRID_UNIT_SIZE
        )
        pygame.draw.rect(surface, COLOR_SHADOW_ZONE, shadow_rect)
        
        # Laser gate
        self.laser_gate.render(surface)
        
        # Goal
        goal_rect = pygame.Rect(
            self.goal['x'] * GRID_UNIT_SIZE,
            self.goal['y'] * GRID_UNIT_SIZE,
            self.goal['width'] * GRID_UNIT_SIZE,
            self.goal['height'] * GRID_UNIT_SIZE
        )
        pygame.draw.rect(surface, COLOR_GOAL, goal_rect)
        
        # Entities
        self.source.render(surface)
        self.shade.render(surface)
        
        # Connection line (helps player understand shadow projection)
        pygame.draw.line(
            surface,
            (64, 64, 64),
            (int(self.source.x * GRID_UNIT_SIZE), int(self.source.y * GRID_UNIT_SIZE)),
            (int(self.shade.x * GRID_UNIT_SIZE), 
             int((self.shade.y + GRID_HEIGHT) * GRID_UNIT_SIZE)),
            1
        )
```

---

## 📦 requirements.txt

```txt
pygame==2.5.2
numpy==1.24.3
```

---

## ✅ Implementation Checklist for Python/Pygame

- [ ] Setup virtual environment and install dependencies
- [ ] Create project structure (game/ directory with subdirectories)
- [ ] Implement config.py with all constants from documentation
- [ ] Implement ShadowProjector class with correct mathematics
- [ ] Implement Source character class with movement and collision
- [ ] Implement Shade class (follows Source shadow)
- [ ] Implement LightSource class
- [ ] Implement LaserGate and bridge spawning
- [ ] Implement Level1 class with exact layout from documentation
- [ ] Implement main game loop with 60 FPS
- [ ] Add death detection system
- [ ] Add win condition
- [ ] Add UI elements (timer, death counter)
- [ ] Test all mechanics thoroughly
- [ ] Ensure visual style matches documentation (minimalist, high-contrast)

---

## 🎯 Python/Pygame Advantages

### Why This Works Well:
✅ **Simple to prototype** - Pure Python, easy to iterate  
✅ **Math-friendly** - Numpy for shadow projection calculations  
✅ **Cross-platform** - Runs on Windows, Mac, Linux  
✅ **Lightweight** - No heavy engine overhead  
✅ **Educational** - Clear code structure, easy to understand  
✅ **Fast development** - Can implement MVP in days, not weeks  

---

## 🚀 Getting Started

```bash
# Clone repository
cd puzzle-game

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python game/main.py
```

---

**Reference**: See all *.md documentation files in repository root for complete game design specifications.

**Technology**: Python 3.11+ with Pygame 2.5.2

**Status**: Ready for implementation by coding agent

**Timeline**: 7 days following LEVEL_1_IMPLEMENTATION.md schedule
