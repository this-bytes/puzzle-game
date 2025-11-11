"""
Laser Gate Mechanism
Projects laser beam that can be blocked by Shade to trigger bridge.
"""

import pygame
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *


class LaserGate:
    """
    Laser gate that projects a beam upward.
    When Shade blocks the beam, triggers bridge spawning.
    """
    
    def __init__(self, x, y, width, height):
        # Position in grid units
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Beam properties
        self.beam_width = 0.5  # units
        self.beam_color = COLOR_LASER
        self.blocked = False
    
    def check_shade_collision(self, shade):
        """
        Check if Shade is blocking the laser beam.
        
        Args:
            shade: Shade entity
            
        Returns:
            True if Shade is blocking the beam
        """
        # Simple AABB collision with the beam hitbox
        beam_x = self.x + (self.width / 2) - (self.beam_width / 2)
        beam_y = self.y
        beam_height = abs(self.y) + 10  # Extends upward
        
        collision = (shade.x < beam_x + self.beam_width and
                    shade.x + shade.width > beam_x and
                    shade.y < beam_y + beam_height and
                    shade.y + shade.height > beam_y)
        
        self.blocked = collision
        return collision
    
    def render(self, surface):
        """Render laser gate and beam."""
        # Convert to pixels
        pixel_x = int(self.x * GRID_UNIT_SIZE)
        pixel_y = int((self.y + GRID_HEIGHT) * GRID_UNIT_SIZE)  # Offset for shadow floor
        pixel_w = int(self.width * GRID_UNIT_SIZE)
        pixel_h = int(self.height * GRID_UNIT_SIZE)
        
        # Draw laser gate base
        gate_rect = pygame.Rect(pixel_x, pixel_y, pixel_w, pixel_h)
        pygame.draw.rect(surface, (100, 100, 100), gate_rect)
        pygame.draw.rect(surface, (150, 150, 150), gate_rect, 2)
        
        # Draw laser beam (projects upward)
        beam_x = int((self.x + self.width / 2) * GRID_UNIT_SIZE)
        beam_start_y = pixel_y
        beam_end_y = int(5 * GRID_UNIT_SIZE)  # Projects to main level
        beam_width_px = int(self.beam_width * GRID_UNIT_SIZE)
        
        # Beam color changes when blocked
        beam_color = (102, 255, 102) if self.blocked else self.beam_color
        beam_alpha = 150 if self.blocked else 100
        
        # Draw beam with transparency
        beam_surface = pygame.Surface((beam_width_px, beam_start_y - beam_end_y), pygame.SRCALPHA)
        pygame.draw.rect(beam_surface, (*beam_color, beam_alpha), 
                        beam_surface.get_rect())
        surface.blit(beam_surface, (beam_x - beam_width_px // 2, beam_end_y))
