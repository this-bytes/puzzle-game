"""
Game Manager - Main game state handler
Enhanced version with menu and tutorial system
"""

import pygame
from config import *
from level import Level1
from ui import UI
from menu import Menu
from tutorial_levels import TutorialLevel1, TutorialLevel2, TutorialLevel3


class GameManager:
    """
    Manages game state and coordinates menu, tutorial, levels and UI.
    """
    
    def __init__(self):
        self.state = "menu"  # "menu", "tutorial", "playing"
        self.menu = Menu()
        self.tutorial_levels = []
        self.current_tutorial_index = 0
        self.level = None
        self.ui = UI()
        
    def start_tutorial(self):
        """Start the tutorial sequence."""
        self.tutorial_levels = [
            TutorialLevel1(),
            TutorialLevel2(),
            TutorialLevel3()
        ]
        self.current_tutorial_index = 0
        self.state = "tutorial"
    
    def start_level1(self):
        """Start Level 1 directly."""
        self.level = Level1()
        self.state = "playing"
    
    def handle_event(self, event):
        """
        Handle pygame events.
        
        Args:
            event: Pygame event
        """
        if self.state == "menu":
            self.menu.handle_event(event)
            
        elif self.state == "tutorial":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset current tutorial level
                    if self.current_tutorial_index < len(self.tutorial_levels):
                        self.tutorial_levels[self.current_tutorial_index].reset()
                elif event.key == pygame.K_ESCAPE:
                    # Return to menu
                    self.state = "menu"
                elif event.key == pygame.K_n:
                    # Skip to next tutorial
                    if self.current_tutorial_index < len(self.tutorial_levels) - 1:
                        self.current_tutorial_index += 1
                    elif self.current_tutorial_index == len(self.tutorial_levels) - 1:
                        # Tutorial complete, go to Level 1
                        self.start_level1()
                        
        elif self.state == "playing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset level
                    self.level.reset()
                elif event.key == pygame.K_ESCAPE:
                    # Return to menu
                    self.state = "menu"
    
    def update(self, dt):
        """
        Update game state.
        
        Args:
            dt: Delta time in seconds
        """
        if self.state == "menu":
            self.menu.update(dt)
            
            # Check for menu action
            action = self.menu.get_action()
            if action == "tutorial":
                self.start_tutorial()
            elif action == "level1":
                self.start_level1()
            elif action == "quit":
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                
        elif self.state == "tutorial":
            if self.current_tutorial_index < len(self.tutorial_levels):
                current_tutorial = self.tutorial_levels[self.current_tutorial_index]
                current_tutorial.update(dt)
                
                # Check if tutorial level is complete
                if current_tutorial.is_complete():
                    pygame.time.wait(1000)  # Brief pause
                    if self.current_tutorial_index < len(self.tutorial_levels) - 1:
                        self.current_tutorial_index += 1
                    else:
                        # All tutorials complete, go to Level 1
                        self.start_level1()
                        
        elif self.state == "playing":
            if self.level:
                self.level.update(dt)
    
    def render(self, surface):
        """
        Render game.
        
        Args:
            surface: Pygame surface to render on
        """
        if self.state == "menu":
            self.menu.render(surface)
            
        elif self.state == "tutorial":
            if self.current_tutorial_index < len(self.tutorial_levels):
                current_tutorial = self.tutorial_levels[self.current_tutorial_index]
                current_tutorial.render(surface)
                
                # Show tutorial progress
                font = pygame.font.Font(None, 24)
                progress_text = f"Tutorial {self.current_tutorial_index + 1}/{len(self.tutorial_levels)} - Press N to skip, ESC for menu"
                text_surf = font.render(progress_text, True, (120, 120, 120))
                surface.blit(text_surf, (10, GAME_HEIGHT - 30))
                
        elif self.state == "playing":
            if self.level:
                self.level.render(surface)
                self.ui.render(surface, self.level)
