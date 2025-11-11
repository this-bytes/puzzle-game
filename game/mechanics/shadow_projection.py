"""
Shadow Projection System
Calculates shadow position based on Source position and Light position.

Formula from MECHANICS_DEEP_DIVE.md:
Shadow Position = Source Pos + (Source Pos - Light Pos) × Extension Factor
Extension Factor = (Shadow Plane Y - Light Y) / (Source Y - Light Y)
"""

import numpy as np


class ShadowProjector:
    """
    Calculates shadow position based on Source position and Light position.
    """
    
    @staticmethod
    def calculate_shade_position(source_pos, light_pos, shadow_plane_y):
        """
        Calculate where the shade appears based on light projection.
        
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
