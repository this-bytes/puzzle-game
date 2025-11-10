#!/usr/bin/env python3
"""
Screenshot generator for the game (headless mode)
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

def take_screenshot(filename="game_screenshot.png"):
    """Take a screenshot of the game state."""
    pygame.init()
    
    # Create window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Create game surface (internal resolution)
    game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    
    # Game manager
    game_manager = GameManager()
    
    # Simulate a few frames to let physics settle
    for _ in range(10):
        game_manager.update(1/60.0)
    
    # Render to game surface
    game_surface.fill(COLOR_BACKGROUND)
    game_manager.render(game_surface)
    
    # Scale and blit to screen
    scaled_surface = pygame.transform.scale(
        game_surface,
        (int(GAME_WIDTH * SCALE_FACTOR), int(GAME_HEIGHT * SCALE_FACTOR))
    )
    screen.fill((0, 0, 0))
    offset_x = (WINDOW_WIDTH - scaled_surface.get_width()) // 2
    offset_y = (WINDOW_HEIGHT - scaled_surface.get_height()) // 2
    screen.blit(scaled_surface, (offset_x, offset_y))
    
    # Save screenshot
    pygame.image.save(screen, filename)
    print(f"Screenshot saved to {filename}")
    
    pygame.quit()

if __name__ == "__main__":
    output_file = sys.argv[1] if len(sys.argv) > 1 else "game_screenshot.png"
    take_screenshot(output_file)
