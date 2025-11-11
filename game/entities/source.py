"""
Source Character - Player-controlled entity
Must stay in light to survive.
"""

import pygame
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
        self.gravity = GRAVITY
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
                # Simple collision response (push up to platform surface)
                if self.velocity_y > 0:  # Falling down
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
