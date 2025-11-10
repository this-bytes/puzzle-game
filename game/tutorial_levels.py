"""
Tutorial Levels - Progressive Introduction to Game Mechanics
Each level teaches one concept at a time
"""

import pygame
from config import *
from entities.source import Source
from entities.shade import Shade
from entities.light_source import LightSource
from mechanics.shadow_projection import ShadowProjector
from mechanics.laser_gate import LaserGate
from mechanics.death_detection import DeathDetector
from tutorial import TutorialManager
from effects import ParticleSystem, LightGlow, ConnectionLine, DeathEffect, BridgeSpawnAnimation


class TutorialLevel1:
    """
    Tutorial 1: Introduction to Source
    Teaches: Basic movement, staying in light
    """
    
    def __init__(self):
        self.platforms = [
            {'x': 0, 'y': 5, 'width': 30, 'height': 2},   # Ground
        ]
        
        self.source = Source(5, 7)
        self.light = LightSource(5, 15, 10)  # Small light directly above
        self.shade = Shade(-2)
        
        self.projector = ShadowProjector()
        self.death_detector = DeathDetector()
        
        self.goal = {'x': 20, 'y': 7, 'width': 3, 'height': 3}
        
        self.deaths = 0
        self.start_time = pygame.time.get_ticks()
        self.completed = False
        
        # Tutorial
        self.tutorial = TutorialManager()
        self.tutorial.add_step(
            "Welcome to Shade & Source!",
            "This is Source (the white character). Use A/D or Arrow Keys to move right.",
            lambda: self.source.x > 10,
            highlight={'x': 3, 'y': 5, 'width': 4, 'height': 4, 'grid': True}
        )
        self.tutorial.add_step(
            "Stay in the Light",
            "Source must stay in the light circle to survive. Try moving outside the light.",
            lambda: self.deaths > 0,
            highlight={'x': self.light.x - 10, 'y': self.light.y - 10, 'width': 20, 'height': 20, 'grid': True}
        )
        self.tutorial.add_step(
            "Reach the Goal",
            "Now reach the green goal area while staying in light. Press R to reset if you die.",
            lambda: self.completed,
            highlight={'x': self.goal['x'], 'y': self.goal['y'], 'width': self.goal['width'], 'height': self.goal['height'], 'grid': True}
        )
        
        # Effects
        self.particles = ParticleSystem()
        self.light_glow = LightGlow(self.light.x, self.light.y, self.light.radius, COLOR_LIGHT_ZONE)
        self.death_effect = DeathEffect()
    
    def update(self, dt):
        """Update tutorial level."""
        if self.completed:
            return
        
        keys = pygame.key.get_pressed()
        self.source.handle_input(keys)
        self.source.update(dt, self.platforms)
        
        shade_pos = self.projector.calculate_shade_position(
            (self.source.x, self.source.y),
            (self.light.x, self.light.y),
            -2
        )
        self.shade.update(shade_pos)
        
        # Check death
        source_dead, reason = self.death_detector.check_source_death(
            self.source, self.projector, self.light
        )
        if source_dead and not self.death_effect.active:
            self.deaths += 1
            self.death_effect.trigger(
                self.source.x * GRID_UNIT_SIZE,
                self.source.y * GRID_UNIT_SIZE,
                (255, 200, 200)
            )
            pygame.time.wait(500)
            self.source.reset()
        
        # Check win
        if self.source.check_collision(self.goal):
            self.completed = True
        
        # Update effects
        self.tutorial.update(dt)
        self.particles.update(dt)
        self.light_glow.update(dt)
        self.death_effect.update(dt)
    
    def render(self, surface):
        """Render tutorial level."""
        # Light glow
        self.light_glow.render(surface)
        
        # Platforms
        for platform in self.platforms:
            rect = pygame.Rect(
                platform['x'] * GRID_UNIT_SIZE,
                platform['y'] * GRID_UNIT_SIZE,
                platform['width'] * GRID_UNIT_SIZE,
                platform['height'] * GRID_UNIT_SIZE
            )
            pygame.draw.rect(surface, COLOR_PLATFORM, rect)
        
        # Light source
        self.light.render(surface)
        
        # Goal
        goal_rect = pygame.Rect(
            self.goal['x'] * GRID_UNIT_SIZE,
            self.goal['y'] * GRID_UNIT_SIZE,
            self.goal['width'] * GRID_UNIT_SIZE,
            self.goal['height'] * GRID_UNIT_SIZE
        )
        pygame.draw.rect(surface, COLOR_GOAL, goal_rect)
        
        # Entities
        self.source.render(surface)
        
        # Effects
        self.particles.render(surface)
        self.death_effect.render(surface)
        
        # Tutorial UI
        self.tutorial.render(surface)
        
        # Stats
        font = pygame.font.Font(None, 24)
        death_text = font.render(f"Deaths: {self.deaths}", True, (200, 200, 200))
        surface.blit(death_text, (GAME_WIDTH - 120, 10))
    
    def reset(self):
        """Reset level."""
        self.source.reset()
        self.completed = False
    
    def is_complete(self):
        """Check if tutorial is complete."""
        return self.tutorial.is_complete() and self.completed


class TutorialLevel2:
    """
    Tutorial 2: Meet the Shade
    Teaches: Shadow projection, dual survival constraint
    """
    
    def __init__(self):
        self.platforms = [
            {'x': 0, 'y': 8, 'width': 15, 'height': 2},   # Left platform
            {'x': 20, 'y': 8, 'width': 10, 'height': 2},  # Right platform
        ]
        
        self.shadow_floor = {'x': 0, 'y': -2, 'width': 30, 'height': 2}
        
        self.source = Source(5, 10)
        self.light = LightSource(7, 18, 14)
        self.shade = Shade(self.shadow_floor['y'])
        
        self.projector = ShadowProjector()
        self.death_detector = DeathDetector()
        
        self.goal = {'x': 22, 'y': 10, 'width': 3, 'height': 3}
        
        self.deaths = 0
        self.start_time = pygame.time.get_ticks()
        self.completed = False
        
        # Tutorial
        self.tutorial = TutorialManager()
        self.tutorial.add_step(
            "Meet Your Shadow",
            "The black figure below is Shade - your shadow. It follows your position relative to the light.",
            lambda: pygame.time.get_ticks() - self.start_time > 3000,
        )
        self.tutorial.add_step(
            "Shade Must Stay in Darkness",
            "Shade dies if it enters light. Move right and watch Shade follow you in the shadows below.",
            lambda: self.source.x > 10,
        )
        self.tutorial.add_step(
            "Dual Survival",
            "Both Source AND Shade must survive. Reach the goal while keeping both alive!",
            lambda: self.completed,
            highlight={'x': self.goal['x'], 'y': self.goal['y'], 'width': self.goal['width'], 'height': self.goal['height'], 'grid': True}
        )
        
        # Effects
        self.particles = ParticleSystem()
        self.light_glow = LightGlow(self.light.x, self.light.y, self.light.radius, COLOR_LIGHT_ZONE)
        self.connection = ConnectionLine()
        self.death_effect = DeathEffect()
    
    def update(self, dt):
        """Update tutorial level."""
        if self.completed:
            return
        
        keys = pygame.key.get_pressed()
        self.source.handle_input(keys)
        self.source.update(dt, self.platforms)
        
        shade_pos = self.projector.calculate_shade_position(
            (self.source.x, self.source.y),
            (self.light.x, self.light.y),
            self.shadow_floor['y']
        )
        self.shade.update(shade_pos)
        
        # Check death
        source_dead, source_reason = self.death_detector.check_source_death(
            self.source, self.projector, self.light
        )
        shade_dead, shade_reason = self.death_detector.check_shade_death(
            self.shade, self.projector, self.light
        )
        
        if (source_dead or shade_dead) and not self.death_effect.active:
            self.deaths += 1
            if source_dead:
                self.death_effect.trigger(
                    self.source.x * GRID_UNIT_SIZE,
                    self.source.y * GRID_UNIT_SIZE,
                    (255, 200, 200)
                )
            else:
                self.death_effect.trigger(
                    self.shade.x * GRID_UNIT_SIZE,
                    (self.shade.y + GRID_HEIGHT) * GRID_UNIT_SIZE,
                    (150, 150, 255)
                )
            pygame.time.wait(500)
            self.source.reset()
        
        # Check win
        if self.source.check_collision(self.goal):
            self.completed = True
        
        # Update effects
        self.tutorial.update(dt)
        self.particles.update(dt)
        self.light_glow.update(dt)
        self.connection.update(dt)
        self.death_effect.update(dt)
    
    def render(self, surface):
        """Render tutorial level."""
        # Light glow
        self.light_glow.render(surface)
        
        # Platforms
        for platform in self.platforms:
            rect = pygame.Rect(
                platform['x'] * GRID_UNIT_SIZE,
                platform['y'] * GRID_UNIT_SIZE,
                platform['width'] * GRID_UNIT_SIZE,
                platform['height'] * GRID_UNIT_SIZE
            )
            pygame.draw.rect(surface, COLOR_PLATFORM, rect)
        
        # Shadow floor
        shadow_rect = pygame.Rect(
            self.shadow_floor['x'] * GRID_UNIT_SIZE,
            (self.shadow_floor['y'] + GRID_HEIGHT) * GRID_UNIT_SIZE,
            self.shadow_floor['width'] * GRID_UNIT_SIZE,
            self.shadow_floor['height'] * GRID_UNIT_SIZE
        )
        pygame.draw.rect(surface, COLOR_SHADOW_ZONE, shadow_rect)
        
        # Light source
        self.light.render(surface)
        
        # Goal
        goal_rect = pygame.Rect(
            self.goal['x'] * GRID_UNIT_SIZE,
            self.goal['y'] * GRID_UNIT_SIZE,
            self.goal['width'] * GRID_UNIT_SIZE,
            self.goal['height'] * GRID_UNIT_SIZE
        )
        pygame.draw.rect(surface, COLOR_GOAL, goal_rect)
        
        # Connection line
        self.connection.render(surface, self.source.x, self.source.y, self.shade.x, self.shade.y)
        
        # Entities
        self.source.render(surface)
        self.shade.render(surface)
        
        # Effects
        self.particles.render(surface)
        self.death_effect.render(surface)
        
        # Tutorial UI
        self.tutorial.render(surface)
        
        # Stats
        font = pygame.font.Font(None, 24)
        death_text = font.render(f"Deaths: {self.deaths}", True, (200, 200, 200))
        surface.blit(death_text, (GAME_WIDTH - 120, 10))
    
    def reset(self):
        """Reset level."""
        self.source.reset()
        self.completed = False
    
    def is_complete(self):
        """Check if tutorial is complete."""
        return self.tutorial.is_complete() and self.completed


class TutorialLevel3:
    """
    Tutorial 3: Shadow Triggers
    Teaches: Using Shade to trigger environmental interactions (laser gate)
    """
    
    def __init__(self):
        self.platforms = [
            {'x': 0, 'y': 8, 'width': 12, 'height': 2},   # Left platform
            {'x': 18, 'y': 8, 'width': 12, 'height': 2},  # Right platform
        ]
        
        self.shadow_floor = {'x': 0, 'y': -2, 'width': 30, 'height': 2}
        
        self.source = Source(5, 10)
        self.light = LightSource(10, 18, 16)
        self.shade = Shade(self.shadow_floor['y'])
        
        self.projector = ShadowProjector()
        self.death_detector = DeathDetector()
        self.laser_gate = LaserGate(12, -5, 6, 8)
        
        self.bridge = None
        self.bridge_active = False
        self.bridge_animation = BridgeSpawnAnimation()
        
        self.goal = {'x': 22, 'y': 10, 'width': 3, 'height': 3}
        
        self.deaths = 0
        self.start_time = pygame.time.get_ticks()
        self.completed = False
        
        # Tutorial
        self.tutorial = TutorialManager()
        self.tutorial.add_step(
            "The Power of Shadows",
            "See the red laser beam? Shade can block it! Move right to position Shade in the beam's path.",
            lambda: self.laser_gate.blocked,
        )
        self.tutorial.add_step(
            "Bridge Appears!",
            "When Shade blocks the laser, a bridge spawns! This is the core mechanic: use your shadow to solve puzzles.",
            lambda: self.bridge_active,
        )
        self.tutorial.add_step(
            "Complete the Tutorial",
            "Cross the bridge and reach the goal. Remember: where you stand determines where you cannot!",
            lambda: self.completed,
            highlight={'x': self.goal['x'], 'y': self.goal['y'], 'width': self.goal['width'], 'height': self.goal['height'], 'grid': True}
        )
        
        # Effects
        self.particles = ParticleSystem()
        self.light_glow = LightGlow(self.light.x, self.light.y, self.light.radius, COLOR_LIGHT_ZONE)
        self.connection = ConnectionLine()
        self.death_effect = DeathEffect()
    
    def update(self, dt):
        """Update tutorial level."""
        if self.completed:
            return
        
        keys = pygame.key.get_pressed()
        self.source.handle_input(keys)
        
        all_platforms = self.platforms.copy()
        if self.bridge_active and self.bridge:
            all_platforms.append(self.bridge)
        
        self.source.update(dt, all_platforms)
        
        shade_pos = self.projector.calculate_shade_position(
            (self.source.x, self.source.y),
            (self.light.x, self.light.y),
            self.shadow_floor['y']
        )
        self.shade.update(shade_pos)
        
        # Check laser gate
        if self.laser_gate.check_shade_collision(self.shade):
            if not self.bridge_active and not self.bridge_animation.animating:
                self.bridge = {'x': 12, 'y': 8, 'width': 6, 'height': 2}
                self.bridge_animation.start(self.bridge)
                # Emit particles
                self.particles.emit(
                    self.bridge['x'] * GRID_UNIT_SIZE,
                    self.bridge['y'] * GRID_UNIT_SIZE,
                    20, (200, 255, 200), spread=80
                )
        
        # Update bridge animation
        if self.bridge_animation.update(dt):
            self.bridge_active = True
        
        # Check death
        source_dead, _ = self.death_detector.check_source_death(
            self.source, self.projector, self.light
        )
        shade_dead, _ = self.death_detector.check_shade_death(
            self.shade, self.projector, self.light
        )
        
        if (source_dead or shade_dead) and not self.death_effect.active:
            self.deaths += 1
            if source_dead:
                self.death_effect.trigger(
                    self.source.x * GRID_UNIT_SIZE,
                    self.source.y * GRID_UNIT_SIZE,
                    (255, 200, 200)
                )
            else:
                self.death_effect.trigger(
                    self.shade.x * GRID_UNIT_SIZE,
                    (self.shade.y + GRID_HEIGHT) * GRID_UNIT_SIZE,
                    (150, 150, 255)
                )
            pygame.time.wait(500)
            self.source.reset()
            self.bridge_active = False
            self.bridge = None
        
        # Check win
        if self.source.check_collision(self.goal):
            self.completed = True
            self.particles.emit(
                self.goal['x'] * GRID_UNIT_SIZE + 48,
                self.goal['y'] * GRID_UNIT_SIZE + 48,
                30, (200, 255, 200), spread=100
            )
        
        # Update effects
        self.tutorial.update(dt)
        self.particles.update(dt)
        self.light_glow.update(dt)
        self.connection.update(dt)
        self.death_effect.update(dt)
    
    def render(self, surface):
        """Render tutorial level."""
        # Light glow
        self.light_glow.render(surface)
        
        # Platforms
        for platform in self.platforms:
            rect = pygame.Rect(
                platform['x'] * GRID_UNIT_SIZE,
                platform['y'] * GRID_UNIT_SIZE,
                platform['width'] * GRID_UNIT_SIZE,
                platform['height'] * GRID_UNIT_SIZE
            )
            pygame.draw.rect(surface, COLOR_PLATFORM, rect)
        
        # Shadow floor
        shadow_rect = pygame.Rect(
            self.shadow_floor['x'] * GRID_UNIT_SIZE,
            (self.shadow_floor['y'] + GRID_HEIGHT) * GRID_UNIT_SIZE,
            self.shadow_floor['width'] * GRID_UNIT_SIZE,
            self.shadow_floor['height'] * GRID_UNIT_SIZE
        )
        pygame.draw.rect(surface, COLOR_SHADOW_ZONE, shadow_rect)
        
        # Light source
        self.light.render(surface)
        
        # Laser gate
        self.laser_gate.render(surface)
        
        # Bridge
        if self.bridge_animation.animating:
            self.bridge_animation.render(surface, self.bridge)
        elif self.bridge_active and self.bridge:
            rect = pygame.Rect(
                self.bridge['x'] * GRID_UNIT_SIZE,
                self.bridge['y'] * GRID_UNIT_SIZE,
                self.bridge['width'] * GRID_UNIT_SIZE,
                self.bridge['height'] * GRID_UNIT_SIZE
            )
            pygame.draw.rect(surface, (160, 160, 160), rect)
        
        # Goal
        goal_rect = pygame.Rect(
            self.goal['x'] * GRID_UNIT_SIZE,
            self.goal['y'] * GRID_UNIT_SIZE,
            self.goal['width'] * GRID_UNIT_SIZE,
            self.goal['height'] * GRID_UNIT_SIZE
        )
        pygame.draw.rect(surface, COLOR_GOAL, goal_rect)
        
        # Connection line
        self.connection.render(surface, self.source.x, self.source.y, self.shade.x, self.shade.y)
        
        # Entities
        self.source.render(surface)
        self.shade.render(surface)
        
        # Effects
        self.particles.render(surface)
        self.death_effect.render(surface)
        
        # Tutorial UI
        self.tutorial.render(surface)
        
        # Stats
        font = pygame.font.Font(None, 24)
        death_text = font.render(f"Deaths: {self.deaths}", True, (200, 200, 200))
        surface.blit(death_text, (GAME_WIDTH - 120, 10))
    
    def reset(self):
        """Reset level."""
        self.source.reset()
        self.bridge_active = False
        self.bridge = None
        self.completed = False
    
    def is_complete(self):
        """Check if tutorial is complete."""
        return self.tutorial.is_complete() and self.completed
