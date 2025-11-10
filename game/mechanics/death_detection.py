"""
Death Detection System
Checks if Source or Shade violate survival constraints.
"""


class DeathDetector:
    """
    Checks death conditions for Source and Shade.
    """
    
    @staticmethod
    def check_source_death(source, projector, light):
        """
        Check if Source died (entered shadow).
        
        Args:
            source: Source entity
            projector: ShadowProjector instance
            light: LightSource entity
            
        Returns:
            (bool, str): (is_dead, reason)
        """
        # Source must be in light
        source_in_light = projector.is_in_light_radius(
            (source.x, source.y),
            (light.x, light.y),
            light.radius
        )
        
        if not source_in_light:
            return (True, "Source entered shadow")
        
        # Check out of bounds (fell into pit)
        if source.y > 20 or source.y < 0:
            return (True, "Source fell out of bounds")
        
        return (False, "")
    
    @staticmethod
    def check_shade_death(shade, projector, light):
        """
        Check if Shade died (entered light).
        
        Args:
            shade: Shade entity
            projector: ShadowProjector instance
            light: LightSource entity
            
        Returns:
            (bool, str): (is_dead, reason)
        """
        # Shade must be in darkness (not in light)
        shade_in_light = projector.is_in_light_radius(
            (shade.x, shade.y),
            (light.x, light.y),
            light.radius
        )
        
        if shade_in_light:
            return (True, "Shade entered light")
        
        return (False, "")
