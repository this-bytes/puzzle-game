"""
Tutorial System for Shade & Source
Guides players through the core mechanics step-by-step
"""

import pygame
from config import *


class TutorialStep:
    """Represents a single tutorial step with instruction and completion condition."""
    
    def __init__(self, title, instruction, check_fn, highlight=None):
        """
        Args:
            title: Short title for the step
            instruction: Text explaining what to do
            check_fn: Function that returns True when step is complete
            highlight: Optional dict with area to highlight {'x', 'y', 'width', 'height'}
        """
        self.title = title
        self.instruction = instruction
        self.check_fn = check_fn
        self.highlight = highlight
        self.completed = False
    
    def check_completion(self):
        """Check if this step is complete."""
        if not self.completed and self.check_fn():
            self.completed = True
        return self.completed


class TutorialManager:
    """Manages tutorial progression and rendering."""
    
    def __init__(self):
        self.steps = []
        self.current_step_index = 0
        self.font_title = pygame.font.Font(None, 32)
        self.font_text = pygame.font.Font(None, 24)
        self.active = True
        self.completion_timer = 0
        
    def add_step(self, title, instruction, check_fn, highlight=None):
        """Add a tutorial step."""
        self.steps.append(TutorialStep(title, instruction, check_fn, highlight))
    
    def update(self, dt):
        """Update tutorial state."""
        if not self.active or self.current_step_index >= len(self.steps):
            return
        
        # Check current step completion
        current_step = self.steps[self.current_step_index]
        if current_step.check_completion():
            self.completion_timer += dt
            if self.completion_timer > 1.0:  # Wait 1 second before next step
                self.completion_timer = 0
                self.current_step_index += 1
                if self.current_step_index >= len(self.steps):
                    self.active = False  # Tutorial complete
    
    def render(self, surface):
        """Render tutorial UI."""
        if not self.active or self.current_step_index >= len(self.steps):
            return
        
        current_step = self.steps[self.current_step_index]
        
        # Render highlight if present
        if current_step.highlight and not current_step.completed:
            self.render_highlight(surface, current_step.highlight)
        
        # Render instruction box
        self.render_instruction_box(surface, current_step)
    
    def render_highlight(self, surface, highlight):
        """Render a pulsing highlight around an area."""
        # Convert grid units to pixels if needed
        if 'grid' in highlight and highlight['grid']:
            x = int(highlight['x'] * GRID_UNIT_SIZE)
            y = int(highlight['y'] * GRID_UNIT_SIZE)
            width = int(highlight['width'] * GRID_UNIT_SIZE)
            height = int(highlight['height'] * GRID_UNIT_SIZE)
        else:
            x, y = highlight['x'], highlight['y']
            width, height = highlight['width'], highlight['height']
        
        # Pulsing effect
        pulse = abs(pygame.time.get_ticks() % 1000 - 500) / 500.0
        alpha = int(100 + 100 * pulse)
        
        # Draw highlight
        highlight_surf = pygame.Surface((width + 20, height + 20), pygame.SRCALPHA)
        pygame.draw.rect(highlight_surf, (255, 255, 100, alpha), highlight_surf.get_rect(), 3)
        surface.blit(highlight_surf, (x - 10, y - 10))
    
    def render_instruction_box(self, surface, step):
        """Render the instruction text box."""
        # Box dimensions
        box_width = GAME_WIDTH - 40
        box_height = 120
        box_x = 20
        box_y = 20
        
        # Background
        box_surf = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        pygame.draw.rect(box_surf, (0, 0, 0, 200), box_surf.get_rect(), border_radius=10)
        pygame.draw.rect(box_surf, (100, 200, 255, 255), box_surf.get_rect(), 2, border_radius=10)
        
        surface.blit(box_surf, (box_x, box_y))
        
        # Title
        title_text = self.font_title.render(step.title, True, (100, 200, 255))
        surface.blit(title_text, (box_x + 20, box_y + 15))
        
        # Instruction (word wrap)
        words = step.instruction.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            line_text = ' '.join(current_line)
            if self.font_text.size(line_text)[0] > box_width - 40:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        y_offset = box_y + 50
        for line in lines:
            text_surf = self.font_text.render(line, True, (220, 220, 220))
            surface.blit(text_surf, (box_x + 20, y_offset))
            y_offset += 25
        
        # Completion indicator
        if step.completed:
            check_text = self.font_title.render("✓", True, (100, 255, 100))
            surface.blit(check_text, (box_x + box_width - 50, box_y + 15))
    
    def is_complete(self):
        """Check if all tutorial steps are complete."""
        return not self.active
    
    def skip(self):
        """Skip the tutorial."""
        self.active = False
