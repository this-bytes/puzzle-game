"""
Game Manager - Main game state handler
"""

import pygame
from config import *
from level import Level1
from ui import UI


class GameManager:
    """
    Manages game state and coordinates level and UI.
    """
    
    def __init__(self):
        self.level = Level1()
        self.ui = UI()
    
    def handle_event(self, event):
        """
        Handle pygame events.
        
        Args:
            event: Pygame event
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset level
                self.level.reset()
    
    def update(self, dt):
        """
        Update game state.
        
        Args:
            dt: Delta time in seconds
        """
        self.level.update(dt)
    
    def render(self, surface):
        """
        Render game.
        
        Args:
            surface: Pygame surface to render on
        """
        self.level.render(surface)
        self.ui.render(surface, self.level)
