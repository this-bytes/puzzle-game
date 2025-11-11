"""
Configuration constants for Shade & Source
All constants from PYTHON_PYGAME_GUIDE.md and LEVEL_1_IMPLEMENTATION.md
"""

import pygame

# Window configuration
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FPS = 60

# Game grid (from documentation)
GRID_UNIT_SIZE = 32  # pixels per unit
GRID_WIDTH = 30      # units
GRID_HEIGHT = 20     # units
GAME_WIDTH = GRID_WIDTH * GRID_UNIT_SIZE   # 960 pixels
GAME_HEIGHT = GRID_HEIGHT * GRID_UNIT_SIZE  # 640 pixels

# Scale factor for display (960x640 → 1920x1080)
SCALE_FACTOR = min(WINDOW_WIDTH / GAME_WIDTH, WINDOW_HEIGHT / GAME_HEIGHT)

# Color palette (exact hex codes from documentation)
COLOR_BACKGROUND = (26, 26, 26)      # #1A1A1A
COLOR_LIGHT_ZONE = (245, 245, 245)   # #F5F5F5
COLOR_SHADOW_ZONE = (13, 13, 13)     # #0D0D0D
COLOR_PLATFORM = (128, 128, 128)     # #808080
COLOR_SOURCE_GLOW = (255, 229, 204)  # #FFE5CC (5% opacity)
COLOR_SHADE_GLOW = (204, 229, 255)   # #CCE5FF (3% opacity)
COLOR_GOAL = (204, 255, 229)         # #CCFFE5
COLOR_LASER = (255, 102, 102)        # #FF6666

# Physics constants
GRAVITY = 20.0  # units per second^2
