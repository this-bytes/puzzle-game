#!/usr/bin/env python3
"""
Generate screenshots of the enhanced MVP
"""

import sys
import os

# Set up SDL to work without display
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pygame
from config import *
from game_manager import GameManager

def take_screenshots():
    """Take screenshots of different game states."""
    pygame.init()
    
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    
    game_manager = GameManager()
    
    # Screenshot 1: Menu
    print("Capturing menu...")
    for _ in range(5):
        game_manager.update(1/60.0)
    game_surface.fill(COLOR_BACKGROUND)
    game_manager.render(game_surface)
    scaled = pygame.transform.scale(game_surface, 
                                    (int(GAME_WIDTH * SCALE_FACTOR), 
                                     int(GAME_HEIGHT * SCALE_FACTOR)))
    final = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    final.fill((0, 0, 0))
    offset_x = (WINDOW_WIDTH - scaled.get_width()) // 2
    offset_y = (WINDOW_HEIGHT - scaled.get_height()) // 2
    final.blit(scaled, (offset_x, offset_y))
    pygame.image.save(final, "/tmp/enhanced_menu.png")
    print("  Saved: /tmp/enhanced_menu.png")
    
    # Screenshot 2: Tutorial Level 1
    print("Capturing tutorial level 1...")
    game_manager.start_tutorial()
    for _ in range(30):
        game_manager.update(1/60.0)
    game_surface.fill(COLOR_BACKGROUND)
    game_manager.render(game_surface)
    scaled = pygame.transform.scale(game_surface,
                                    (int(GAME_WIDTH * SCALE_FACTOR),
                                     int(GAME_HEIGHT * SCALE_FACTOR)))
    final = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    final.fill((0, 0, 0))
    final.blit(scaled, (offset_x, offset_y))
    pygame.image.save(final, "/tmp/enhanced_tutorial1.png")
    print("  Saved: /tmp/enhanced_tutorial1.png")
    
    # Screenshot 3: Tutorial Level 2 (with shade)
    print("Capturing tutorial level 2...")
    game_manager.current_tutorial_index = 1
    for _ in range(30):
        game_manager.update(1/60.0)
    game_surface.fill(COLOR_BACKGROUND)
    game_manager.render(game_surface)
    scaled = pygame.transform.scale(game_surface,
                                    (int(GAME_WIDTH * SCALE_FACTOR),
                                     int(GAME_HEIGHT * SCALE_FACTOR)))
    final = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    final.fill((0, 0, 0))
    final.blit(scaled, (offset_x, offset_y))
    pygame.image.save(final, "/tmp/enhanced_tutorial2.png")
    print("  Saved: /tmp/enhanced_tutorial2.png")
    
    # Screenshot 4: Tutorial Level 3 (with laser gate)
    print("Capturing tutorial level 3...")
    game_manager.current_tutorial_index = 2
    for _ in range(30):
        game_manager.update(1/60.0)
    game_surface.fill(COLOR_BACKGROUND)
    game_manager.render(game_surface)
    scaled = pygame.transform.scale(game_surface,
                                    (int(GAME_WIDTH * SCALE_FACTOR),
                                     int(GAME_HEIGHT * SCALE_FACTOR)))
    final = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    final.fill((0, 0, 0))
    final.blit(scaled, (offset_x, offset_y))
    pygame.image.save(final, "/tmp/enhanced_tutorial3.png")
    print("  Saved: /tmp/enhanced_tutorial3.png")
    
    pygame.quit()
    print("\nAll screenshots generated successfully!")

if __name__ == "__main__":
    take_screenshots()
