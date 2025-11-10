"""
Light Source Entity
Static omnidirectional light that illuminates the scene.
"""

import pygame
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *


class LightSource:
    """
    Static omnidirectional light source.
    Radiates light in all directions.
    """
    
    def __init__(self, x, y, radius):
        # Position in grid units
        self.x = x
        self.y = y
        
        # Light properties
        self.radius = radius  # in grid units
        self.color = COLOR_LIGHT_ZONE
    
    def render(self, surface):
        """Render light source."""
        # Convert to pixels
        pixel_x = int(self.x * GRID_UNIT_SIZE)
        pixel_y = int(self.y * GRID_UNIT_SIZE)
        pixel_radius = int(self.radius * GRID_UNIT_SIZE)
        
        # Draw light radius (very subtle)
        light_surface = pygame.Surface((pixel_radius * 2, pixel_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(light_surface, (*COLOR_LIGHT_ZONE, 10), 
                         (pixel_radius, pixel_radius), pixel_radius)
        surface.blit(light_surface, (pixel_x - pixel_radius, pixel_y - pixel_radius))
        
        # Draw light source itself (small bright circle)
        pygame.draw.circle(surface, COLOR_LIGHT_ZONE, (pixel_x, pixel_y), 6)
        pygame.draw.circle(surface, (255, 255, 255), (pixel_x, pixel_y), 3)
