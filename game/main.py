"""
Shade & Source - Level 1: The Basic Divide
Main entry point for the game.
"""

import pygame
import sys
from config import *
from game_manager import GameManager


def main():
    """Main game loop."""
    pygame.init()
    
    # Create window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Shade & Source - Level 1: The Basic Divide")
    
    # Create game surface (internal resolution)
    game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    
    # Clock for FPS
    clock = pygame.time.Clock()
    
    # Game manager
    game_manager = GameManager()
    
    # Main loop
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            game_manager.handle_event(event)
        
        # Update
        game_manager.update(dt)
        
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
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
