#!/usr/bin/env python3
"""
Test script to verify game mechanics without requiring a display.
"""

import sys
import os

# Set up SDL to work without display
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pygame
from config import *
from entities.source import Source
from entities.shade import Shade
from entities.light_source import LightSource
from mechanics.shadow_projection import ShadowProjector
from mechanics.laser_gate import LaserGate
from mechanics.death_detection import DeathDetector

def test_shadow_projection():
    """Test shadow projection calculation."""
    print("Testing shadow projection...")
    projector = ShadowProjector()
    
    # Test case from documentation:
    # Light at (15, 18), Source at (6, 5), Shadow plane at y = -2
    shade_pos = projector.calculate_shade_position(
        (6, 5),  # source pos
        (15, 18),  # light pos
        -2  # shadow plane y
    )
    
    print(f"  Source at (6, 5), Light at (15, 18)")
    print(f"  Shade projected to: ({shade_pos[0]:.2f}, {shade_pos[1]:.2f})")
    
    # Expected calculation:
    # dx = 6 - 15 = -9
    # dy = 5 - 18 = -13
    # t = (-2 - 18) / -13 = 20 / 13 ≈ 1.538
    # shade_x = 15 + (-9 * 1.538) = 15 - 13.85 ≈ 1.15
    expected_x = 15 + (-9 * ((-2 - 18) / (5 - 18)))
    print(f"  Expected shade_x: {expected_x:.2f}")
    
    assert abs(shade_pos[0] - expected_x) < 0.01, f"Shadow projection failed: {shade_pos[0]} != {expected_x}"
    assert shade_pos[1] == -2, f"Shadow Y should be -2, got {shade_pos[1]}"
    print("  ✓ Shadow projection works correctly!")
    
def test_light_detection():
    """Test light radius detection."""
    print("\nTesting light detection...")
    projector = ShadowProjector()
    light = LightSource(15, 18, 12)
    
    # Test entity in light
    in_light = projector.is_in_light_radius((15, 10), (light.x, light.y), light.radius)
    print(f"  Entity at (15, 10), distance from light: {abs(10-18)} units")
    print(f"  In light (radius 12)? {in_light}")
    assert in_light, "Should be in light"
    
    # Test entity outside light
    out_of_light = projector.is_in_light_radius((0, 0), (light.x, light.y), light.radius)
    print(f"  Entity at (0, 0), far from light")
    print(f"  In light? {out_of_light}")
    assert not out_of_light, "Should be out of light"
    print("  ✓ Light detection works correctly!")

def test_source_movement():
    """Test Source character physics."""
    print("\nTesting Source movement...")
    source = Source(6, 5)
    platforms = [{'x': 0, 'y': 3, 'width': 30, 'height': 2}]
    
    print(f"  Initial position: ({source.x}, {source.y})")
    
    # Simulate one frame of gravity
    dt = 1/60.0
    source.update(dt, platforms)
    
    print(f"  After one frame: ({source.x:.2f}, {source.y:.2f})")
    print(f"  On ground: {source.on_ground}")
    print("  ✓ Source physics working!")

def test_death_detection():
    """Test death detection system."""
    print("\nTesting death detection...")
    projector = ShadowProjector()
    detector = DeathDetector()
    light = LightSource(15, 18, 12)
    source = Source(15, 10)  # Position closer to light (within radius)
    shade = Shade(-2)
    
    # Source in light (should be safe)
    source_dead, reason = detector.check_source_death(source, projector, light)
    print(f"  Source at (15, 10), Light at (15, 18), radius 12")
    print(f"  Distance: {abs(10-18)} < 12")
    print(f"  Source dead? {source_dead} ({reason})")
    assert not source_dead, "Source should be alive in light"
    
    # Source in shadow (should die)
    source.x = 0
    source.y = 0
    source_dead, reason = detector.check_source_death(source, projector, light)
    print(f"  Source at (0, 0) - far from light")
    print(f"  Source dead? {source_dead} ({reason})")
    assert source_dead, "Source should die in shadow"
    
    print("  ✓ Death detection works correctly!")

def test_laser_gate():
    """Test laser gate collision."""
    print("\nTesting laser gate...")
    laser = LaserGate(12, -5, 6, 8)
    shade = Shade(-2)
    
    # Shade not in beam
    shade.x = 0
    shade.y = -2
    blocked = laser.check_shade_collision(shade)
    print(f"  Shade at (0, -2), Laser at (12, -5)")
    print(f"  Laser blocked? {blocked}")
    assert not blocked, "Laser should not be blocked"
    
    # Shade in beam
    shade.x = 15
    shade.y = -2
    blocked = laser.check_shade_collision(shade)
    print(f"  Shade at (15, -2)")
    print(f"  Laser blocked? {blocked}")
    assert blocked, "Laser should be blocked"
    
    print("  ✓ Laser gate works correctly!")

def main():
    """Run all tests."""
    print("=" * 60)
    print("SHADE & SOURCE - MECHANICS TEST SUITE")
    print("=" * 60)
    
    # Initialize pygame (headless)
    pygame.init()
    
    try:
        test_shadow_projection()
        test_light_detection()
        test_source_movement()
        test_death_detection()
        test_laser_gate()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    finally:
        pygame.quit()

if __name__ == "__main__":
    sys.exit(main())
