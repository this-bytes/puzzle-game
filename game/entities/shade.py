"""
Shade Entity - Shadow character
Must stay in darkness to survive.
"""

import pygame
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *


class Shade:
    """
    The Shade (shadow) entity.
    Position is calculated from Source + Light geometry.
    Must stay in darkness to survive.
    """
    
    def __init__(self, shadow_plane_y):
        # Position in grid units (calculated dynamically)
        self.x = 0
        self.y = shadow_plane_y
        self.shadow_plane_y = shadow_plane_y
        
        # Size (matches Source)
        self.width = 0.31  # grid units
        self.height = 0.625  # grid units
        
        # State
        self.alive = True
    
    def update(self, shade_pos):
        """Update position based on shadow projection calculation."""
        self.x, self.y = shade_pos
    
    def render(self, surface):
        """Render Shade entity."""
        # Convert grid units to pixels
        # Note: Shade is on shadow floor at negative Y, so we offset for display
        pixel_x = int(self.x * GRID_UNIT_SIZE)
        pixel_y = int((self.y + GRID_HEIGHT) * GRID_UNIT_SIZE)  # Offset for display
        pixel_w = int(self.width * GRID_UNIT_SIZE)
        pixel_h = int(self.height * GRID_UNIT_SIZE)
        
        # Draw geometric humanoid (same shape as Source, but dark)
        # Head (circle)
        head_radius = pixel_w // 2
        head_center = (pixel_x + pixel_w // 2, pixel_y + head_radius)
        pygame.draw.circle(surface, (0, 0, 0), head_center, head_radius)
        
        # Body (rectangle)
        body_rect = pygame.Rect(
            pixel_x + pixel_w // 4,
            pixel_y + head_radius * 2,
            pixel_w // 2,
            pixel_h - head_radius * 2
        )
        pygame.draw.rect(surface, (0, 0, 0), body_rect)
        
        # Glow effect (optional - 3% opacity)
        glow_surface = pygame.Surface((pixel_w + 10, pixel_h + 10), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (*COLOR_SHADE_GLOW, 8), 
                         (pixel_w // 2 + 5, pixel_h // 2 + 5), 
                         max(pixel_w, pixel_h) // 2 + 5)
        surface.blit(glow_surface, (pixel_x - 5, pixel_y - 5))
