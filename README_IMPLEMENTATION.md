# Shade & Source - Level 1 MVP Implementation

## 🎮 Python + Pygame Implementation

This is the Level 1 prototype implementation of **Shade & Source** using Python 3.12 and Pygame 2.5.2.

### 🚀 Quick Start

```bash
# Install dependencies (Ubuntu/Debian)
sudo apt-get install python3-pygame python3-numpy

# Or using pip (if available)
pip install pygame==2.5.2 numpy==1.24.3

# Run the game
cd game
python3 main.py
```

### 🎯 Controls

- **A / Left Arrow**: Move left
- **D / Right Arrow**: Move right
- **Space / W**: Jump
- **R**: Reset level
- **ESC**: Quit game

### 📁 Project Structure

```
puzzle-game/
├── game/                          # Python implementation
│   ├── main.py                    # Entry point with 60 FPS game loop
│   ├── config.py                  # Constants (colors, grid, physics)
│   ├── level.py                   # Level 1 implementation
│   ├── game_manager.py            # Game state management
│   ├── ui.py                      # UI elements (timer, death counter)
│   ├── test_mechanics.py          # Test suite for mechanics
│   ├── entities/
│   │   ├── source.py              # Source character (player)
│   │   ├── shade.py               # Shade entity (shadow)
│   │   └── light_source.py        # Light source
│   └── mechanics/
│       ├── shadow_projection.py   # Shadow calculation (CRITICAL)
│       ├── death_detection.py     # Safety checking
│       └── laser_gate.py          # Laser gate + bridge mechanics
├── requirements.txt               # Python dependencies
├── .gitignore                     # Python/Pygame gitignore
└── *.md                          # Game design documentation
```

### 🔬 Testing

Run the mechanics test suite to verify all systems:

```bash
cd game
python3 test_mechanics.py
```

All core mechanics are tested:
- ✓ Shadow projection mathematics
- ✓ Light radius detection
- ✓ Source physics and movement
- ✓ Death detection (Source/Shade)
- ✓ Laser gate collision

### 🎮 How to Play

**Objective**: Guide Source to the goal while keeping both Source and Shade alive.

**Rules**:
1. **Source** (white character) must stay in **light** - dies in shadow
2. **Shade** (black shadow) must stay in **darkness** - dies in light
3. Shade's position is determined by Source's position relative to the light
4. Use Shade to block the laser gate, spawning a bridge across the gap
5. Cross the bridge and reach the green goal area to win

**Level 1 Solution**:
1. Move Source right (stays in light)
2. Shade moves along shadow floor below
3. When Shade blocks the laser beam, a bridge appears
4. Jump onto the bridge and reach the goal

### 📊 Features Implemented

- [x] Pure Python + Pygame (no game engines)
- [x] 60 FPS game loop with proper delta time
- [x] Source character with physics (gravity, jumping, collision)
- [x] Real-time shadow projection using mathematical formula
- [x] Light source with radius detection
- [x] Shade entity following Source via shadow projection
- [x] Death detection (Source in shadow, Shade in light)
- [x] Laser gate that detects Shade blocking
- [x] Bridge spawning mechanic
- [x] Goal and win condition
- [x] Timer and death counter UI
- [x] Level reset functionality
- [x] Minimalist high-contrast visual style
- [x] Exact coordinates from LEVEL_1_IMPLEMENTATION.md

### 🎨 Visual Style

Following the documentation specifications:
- **Background**: #1A1A1A (near-black)
- **Light Zones**: #F5F5F5 (off-white)
- **Shadow Zones**: #0D0D0D (pure black)
- **Platforms**: #808080 (grey)
- **Goal**: #CCFFE5 (mint green)
- **Minimalist geometric shapes** - no image assets
- **High contrast** for clarity

### ⚙️ Technical Details

**Grid System**:
- 30 units wide × 20 units tall
- 32 pixels per unit
- Internal resolution: 960×640
- Scaled to 1920×1080 for display

**Shadow Projection Formula** (from MECHANICS_DEEP_DIVE.md):
```
shade_x = light_x + (source_x - light_x) × t
where t = (shadow_plane_y - light_y) / (source_y - light_y)
```

**Physics**:
- Gravity: 20 units/s²
- Source speed: 4 units/s
- Jump force: -10 units/s

### 🐛 Known Issues

- **Light Radius**: Adjusted to 16 units (from documented 12) to ensure Source starts within light at position (6, 5). The mathematical distance from (6, 5) to light at (15, 18) is ~15.8 units.

### 📝 Development Notes

This implementation follows the specifications in:
- `PYTHON_PYGAME_GUIDE.md` - Primary implementation reference
- `LEVEL_1_IMPLEMENTATION.md` - Exact coordinates and layout
- `MECHANICS_DEEP_DIVE.md` - Shadow projection mathematics
- `README.md` - Game concept overview
- `QUICK_REFERENCE.md` - Quick specs reference

**Technology Stack**:
- Python 3.12 (compatible with 3.11+ requirement)
- Pygame 2.5.2 (exact version from requirements)
- NumPy 1.26.4 (for shadow calculations)

### 🎯 Success Criteria

✅ All mechanics functional:
- Source movement and physics
- Shadow projection (mathematically correct)
- Death detection
- Laser gate trigger
- Bridge spawning
- Win condition

✅ Performance:
- Maintains 60 FPS
- No crashes or errors

✅ Visual Style:
- Matches documentation
- Minimalist, high-contrast
- Clear visual feedback

✅ Playability:
- Completable from start to finish
- Controls responsive
- Rules clear through gameplay

### 🚀 Next Steps

For extending beyond Level 1:
1. Add more levels (see LEVEL_1_IMPLEMENTATION.md for patterns)
2. Implement rotatable lights (Level 2 mechanic)
3. Add patrol lights (timing mechanic)
4. Implement prism splitters (multi-shadow mechanic)
5. Add inversion fields (rule reversal mechanic)
6. Polish animations and audio
7. Add tutorial prompts

### 📜 License

This implementation is based on the comprehensive game design documentation in this repository.

**"Where you stand determines where you cannot."** 🌓
