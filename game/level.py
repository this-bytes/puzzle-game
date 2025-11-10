"""
Level 1: The Basic Divide
Exact layout from LEVEL_1_IMPLEMENTATION.md
"""

import pygame
from config import *
from entities.source import Source
from entities.shade import Shade
from entities.light_source import LightSource
from mechanics.shadow_projection import ShadowProjector
from mechanics.laser_gate import LaserGate
from mechanics.death_detection import DeathDetector


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
        # Light radius adjusted to 16 to ensure Source starts in light (distance is ~15.8)
        self.light = LightSource(15, 18, 16)  # Position, radius (adjusted for geometry)
        self.shade = Shade(self.shadow_floor['y'])
        
        # Mechanics
        self.projector = ShadowProjector()
        self.laser_gate = LaserGate(12, -5, 6, 8)  # Position, size from docs
        self.death_detector = DeathDetector()
        
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
        if self.completed:
            return
        
        # Update Source
        keys = pygame.key.get_pressed()
        self.source.handle_input(keys)
        
        # Platforms including bridge if active
        all_platforms = self.platforms.copy()
        if self.bridge_active and self.bridge:
            all_platforms.append(self.bridge)
        
        self.source.update(dt, all_platforms)
        
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
        # Check Source death
        source_dead, source_reason = self.death_detector.check_source_death(
            self.source, self.projector, self.light
        )
        if source_dead:
            self.death_reset(source_reason)
            return
        
        # Check Shade death
        shade_dead, shade_reason = self.death_detector.check_shade_death(
            self.shade, self.projector, self.light
        )
        if shade_dead:
            self.death_reset(shade_reason)
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
        source_pixel_x = int(self.source.x * GRID_UNIT_SIZE)
        source_pixel_y = int(self.source.y * GRID_UNIT_SIZE)
        shade_pixel_x = int(self.shade.x * GRID_UNIT_SIZE)
        shade_pixel_y = int((self.shade.y + GRID_HEIGHT) * GRID_UNIT_SIZE)
        
        pygame.draw.line(
            surface,
            (64, 64, 64),
            (source_pixel_x, source_pixel_y),
            (shade_pixel_x, shade_pixel_y),
            1
        )
    
    def reset(self):
        """Reset level completely."""
        self.source.reset()
        self.bridge_active = False
        self.bridge = None
        self.completed = False
        self.start_time = pygame.time.get_ticks()
