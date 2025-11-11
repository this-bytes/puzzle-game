"""
Visual Effects System
Adds particle effects, animations, and visual polish
"""

import pygame
import random
import math
from config import *


class Particle:
    """Single particle for effects."""
    
    def __init__(self, x, y, vx, vy, color, lifetime, size=3):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.size = size
    
    def update(self, dt):
        """Update particle."""
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += 200 * dt  # Gravity
        self.lifetime -= dt
        return self.lifetime > 0
    
    def render(self, surface):
        """Render particle."""
        alpha = int(255 * (self.lifetime / self.max_lifetime))
        size = int(self.size * (self.lifetime / self.max_lifetime))
        if size > 0:
            surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*self.color, alpha), (size, size), size)
            surface.blit(surf, (int(self.x - size), int(self.y - size)))


class ParticleSystem:
    """Manages all particle effects."""
    
    def __init__(self):
        self.particles = []
    
    def emit(self, x, y, count, color, spread=100, lifetime=1.0):
        """Emit particles."""
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(20, spread)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.particles.append(Particle(x, y, vx, vy, color, lifetime))
    
    def update(self, dt):
        """Update all particles."""
        self.particles = [p for p in self.particles if p.update(dt)]
    
    def render(self, surface):
        """Render all particles."""
        for p in self.particles:
            p.render(surface)
    
    def clear(self):
        """Clear all particles."""
        self.particles.clear()


class LightGlow:
    """Animated light glow effect."""
    
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.base_radius = radius
        self.color = color
        self.pulse_time = 0
    
    def update(self, dt):
        """Update glow animation."""
        self.pulse_time += dt
    
    def render(self, surface):
        """Render glowing light."""
        # Pulsing radius
        pulse = math.sin(self.pulse_time * 2) * 0.1 + 1.0
        radius = int(self.base_radius * GRID_UNIT_SIZE * pulse)
        
        # Multiple layers for glow effect
        for i in range(5, 0, -1):
            alpha = int(30 / i)
            layer_radius = radius * (1 + i * 0.2)
            surf = pygame.Surface((layer_radius * 2, layer_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*self.color, alpha), 
                             (layer_radius, layer_radius), layer_radius)
            surface.blit(surf, (int(self.x * GRID_UNIT_SIZE - layer_radius),
                              int(self.y * GRID_UNIT_SIZE - layer_radius)))


class ConnectionLine:
    """Animated connection line between Source and Shade."""
    
    def __init__(self):
        self.dash_offset = 0
    
    def update(self, dt):
        """Update animation."""
        self.dash_offset += dt * 50
        if self.dash_offset > 20:
            self.dash_offset = 0
    
    def render(self, surface, source_x, source_y, shade_x, shade_y):
        """Render connection line with animation."""
        # Convert to pixels
        sx = int(source_x * GRID_UNIT_SIZE)
        sy = int(source_y * GRID_UNIT_SIZE)
        # Shade Y needs offset for display
        shx = int(shade_x * GRID_UNIT_SIZE)
        shy = int((shade_y + GRID_HEIGHT) * GRID_UNIT_SIZE)
        
        # Draw dashed line
        dx = shx - sx
        dy = shy - sy
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist > 0:
            steps = int(dist / 10)
            for i in range(steps):
                t = i / steps
                if (i + int(self.dash_offset / 10)) % 2 == 0:
                    x = sx + dx * t
                    y = sy + dy * t
                    x2 = sx + dx * (t + 0.05)
                    y2 = sy + dy * (t + 0.05)
                    pygame.draw.line(surface, (100, 150, 200), (x, y), (x2, y2), 2)


class DeathEffect:
    """Death animation effect."""
    
    def __init__(self):
        self.active = False
        self.timer = 0
        self.max_time = 0.5
        self.particles = []
    
    def trigger(self, x, y, color):
        """Trigger death effect."""
        self.active = True
        self.timer = 0
        self.particles.clear()
        
        # Emit particles
        for _ in range(30):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(50, 150)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.particles.append(Particle(x, y, vx, vy, color, 1.0, size=4))
    
    def update(self, dt):
        """Update effect."""
        if not self.active:
            return
        
        self.timer += dt
        self.particles = [p for p in self.particles if p.update(dt)]
        
        if self.timer >= self.max_time and not self.particles:
            self.active = False
    
    def render(self, surface):
        """Render effect."""
        for p in self.particles:
            p.render(surface)


class BridgeSpawnAnimation:
    """Bridge spawning animation."""
    
    def __init__(self):
        self.animating = False
        self.progress = 0
        self.target_bridge = None
    
    def start(self, bridge_data):
        """Start animation."""
        self.animating = True
        self.progress = 0
        self.target_bridge = bridge_data
    
    def update(self, dt):
        """Update animation."""
        if not self.animating:
            return False
        
        self.progress += dt * 2  # 0.5 seconds to complete
        if self.progress >= 1.0:
            self.progress = 1.0
            self.animating = False
            return True
        return False
    
    def render(self, surface, bridge_data):
        """Render animating bridge."""
        if not bridge_data:
            return
        
        # Ease-out effect
        t = 1 - (1 - self.progress) ** 3
        
        # Render partial bridge
        current_width = bridge_data['width'] * t
        
        rect = pygame.Rect(
            bridge_data['x'] * GRID_UNIT_SIZE,
            bridge_data['y'] * GRID_UNIT_SIZE,
            int(current_width * GRID_UNIT_SIZE),
            bridge_data['height'] * GRID_UNIT_SIZE
        )
        
        # Color shifts during animation
        base_color = 160
        glow = int(50 * (1 - t))
        color = (base_color + glow, base_color + glow, base_color + glow)
        
        pygame.draw.rect(surface, color, rect)
        
        # Particles during spawn
        if self.animating:
            # Emit sparkles at the edge
            edge_x = rect.x + rect.width
            edge_y = rect.y + rect.height // 2
            if random.random() < 0.3:
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(20, 50)
                vx = math.cos(angle) * speed
                vy = math.sin(angle) * speed
                # Add to global particle system would be better, but for now just visual
