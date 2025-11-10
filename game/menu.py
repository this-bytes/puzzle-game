"""
Menu System for Shade & Source
"""

import pygame
from config import *


class MenuItem:
    """A single menu item."""
    
    def __init__(self, text, action):
        self.text = text
        self.action = action
        self.hovered = False
    
    def render(self, surface, x, y, font):
        """Render menu item."""
        color = (255, 255, 150) if self.hovered else (200, 200, 200)
        text_surf = font.render(self.text, True, color)
        text_rect = text_surf.get_rect(center=(x, y))
        surface.blit(text_surf, text_rect)
        return text_rect


class Menu:
    """Main menu system."""
    
    def __init__(self):
        self.title_font = pygame.font.Font(None, 72)
        self.menu_font = pygame.font.Font(None, 42)
        self.tagline_font = pygame.font.Font(None, 32)
        
        self.items = [
            MenuItem("Tutorial", "tutorial"),
            MenuItem("Play Level 1", "level1"),
            MenuItem("Quit", "quit")
        ]
        
        self.selected_index = 0
        self.action = None
    
    def handle_event(self, event):
        """Handle menu input."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.selected_index = (self.selected_index - 1) % len(self.items)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.selected_index = (self.selected_index + 1) % len(self.items)
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.action = self.items[self.selected_index].action
        
        # Update hover states
        for i, item in enumerate(self.items):
            item.hovered = (i == self.selected_index)
    
    def update(self, dt):
        """Update menu state."""
        pass
    
    def render(self, surface):
        """Render menu."""
        # Background
        surface.fill(COLOR_BACKGROUND)
        
        # Title
        title = "SHADE & SOURCE"
        title_surf = self.title_font.render(title, True, (200, 230, 255))
        title_rect = title_surf.get_rect(center=(GAME_WIDTH // 2, 150))
        surface.blit(title_surf, title_rect)
        
        # Tagline
        tagline = '"Where you stand determines where you cannot."'
        tagline_surf = self.tagline_font.render(tagline, True, (150, 180, 200))
        tagline_rect = tagline_surf.get_rect(center=(GAME_WIDTH // 2, 200))
        surface.blit(tagline_surf, tagline_rect)
        
        # Menu items
        start_y = 300
        spacing = 60
        
        for i, item in enumerate(self.items):
            y = start_y + i * spacing
            item.render(surface, GAME_WIDTH // 2, y, self.menu_font)
        
        # Instructions
        inst_font = pygame.font.Font(None, 24)
        inst_text = "Use ↑↓ or WS to select, ENTER to confirm"
        inst_surf = inst_font.render(inst_text, True, (120, 120, 120))
        inst_rect = inst_surf.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT - 50))
        surface.blit(inst_surf, inst_rect)
    
    def get_action(self):
        """Get and clear the selected action."""
        action = self.action
        self.action = None
        return action
