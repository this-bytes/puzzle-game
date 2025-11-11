"""
UI Elements - Timer and Death Counter
"""

import pygame
from config import *


class UI:
    """
    Handles UI rendering for timer and death counter.
    """
    
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
    
    def render(self, surface, level):
        """
        Render UI elements.
        
        Args:
            surface: Pygame surface to render on
            level: Level instance to get data from
        """
        # Calculate elapsed time
        elapsed = (pygame.time.get_ticks() - level.start_time) / 1000.0
        
        # Render timer
        time_text = f"Time: {elapsed:.1f}s"
        time_surface = self.font.render(time_text, True, (200, 200, 200))
        surface.blit(time_surface, (10, 10))
        
        # Render death counter
        death_text = f"Deaths: {level.deaths}"
        death_surface = self.font.render(death_text, True, (200, 200, 200))
        surface.blit(death_surface, (10, 50))
        
        # Render completion message if completed
        if level.completed:
            complete_text = "LEVEL COMPLETE!"
            complete_surface = self.font.render(complete_text, True, COLOR_GOAL)
            text_rect = complete_surface.get_rect(center=(GAME_WIDTH // 2, 100))
            surface.blit(complete_surface, text_rect)
            
            # Instructions
            instruct_text = "Press R to restart"
            instruct_surface = self.small_font.render(instruct_text, True, (200, 200, 200))
            instruct_rect = instruct_surface.get_rect(center=(GAME_WIDTH // 2, 140))
            surface.blit(instruct_surface, instruct_rect)
        
        # Render instructions at bottom
        controls_text = "Controls: A/D - Move, SPACE - Jump, R - Reset"
        controls_surface = self.small_font.render(controls_text, True, (150, 150, 150))
        surface.blit(controls_surface, (10, GAME_HEIGHT - 30))
