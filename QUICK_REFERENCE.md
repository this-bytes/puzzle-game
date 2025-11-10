# 🌓 SHADE & SOURCE - Quick Reference Cheat Sheet

## 🎯 Core Rules (The Foundation)

| Entity | Safe In | Dies In | Control |
|--------|---------|---------|---------|
| **Source** | Light | Shadow | Player-controlled |
| **Shade** | Darkness | Light | Follows Source (projected) |

**Win Condition**: Both entities reach goal state simultaneously

---

## 💡 Light Source Types

| Type | Behavior | Player Control | Primary Use |
|------|----------|---------------|-------------|
| **Static Omni** | Fixed position, all directions | None | Foundation puzzles |
| **Static Directional** | Fixed position, cone beam | Rotation only | Precision puzzles |
| **Moveable** | Can be pushed/pulled | Full position | Player-authored solutions |
| **Patrol** | Automated path movement | Indirect (speed/pause) | Timing challenges |
| **Prism** | Splits light into beams | Rotation | Multi-shadow puzzles |

---

## 🗺️ Tutorial Level Progression

### Level 1: Basic Divide
**Teaches**: Core constraints  
**Mechanic**: Shade blocks laser → bridge appears  
**Duration**: 1-2 minutes  

### Level 2: Rotational Geometry  
**Teaches**: Multi-plane projection  
**Mechanic**: Rotate light 45° → shadow moves from floor to wall  
**Duration**: 3-5 minutes  

### Level 3: Interacting Shadows  
**Teaches**: Environmental shadows  
**Mechanic**: Use block shadow + moveable lamp  
**Duration**: 5-8 minutes  

---

## 🔧 Three Advanced Mechanics

### 1️⃣ Patrol Light
```
Rail ════●════════●════
         ↓        ↓
      [Moving Light]
```
- **Adds**: Timing/rhythm element
- **Difficulty**: Medium
- **Key Puzzle**: Wait for safe window to move

### 2️⃣ Prism Splitter
```
    Light → [Prism] → 3 Beams
                       3 Shadows
```
- **Adds**: Multi-constraint management
- **Difficulty**: High
- **Key Puzzle**: ALL shadows must be safe

### 3️⃣ Inversion Field
```
Normal | Inverted | Normal
Light  | Shadow   | Light
Safe   | Safe     | Safe
```
- **Adds**: Mental model reversal
- **Difficulty**: Very High
- **Key Puzzle**: Cross boundary at right moment

---

## 🎨 Visual Style Guide

### Color Palette
```
Background:  #1A1A1A (near-black)
Light:       #F5F5F5 (off-white)
Shadow:      #0D0D0D (pure black)
Neutral:     #808080 (mid-grey)

Accents (5-10% opacity):
Source:      #FFE5CC (warm peach)
Shade:       #CCE5FF (cool blue)
Inversion:   #E5CCFF (purple)
```

### Character Design
```
Source:  ● (white, warm glow)
        ╱│╲
         │
        ╱ ╲

Shade:   ● (black, cool glow)
        ╱│╲
         │
        ╱ ╲ (exact silhouette)
```

---

## 🎮 Control Scheme

| Action | Keyboard | Gamepad | Touch |
|--------|----------|---------|-------|
| Move Left | A / ← | D-Pad Left | Swipe Left |
| Move Right | D / → | D-Pad Right | Swipe Right |
| Jump | Space / W | A Button | Tap Screen |
| Interact | E | X Button | Tap Object |
| Reset Level | R | Select | Pause → Reset |
| Pause | Esc | Start | Three-finger Tap |

---

## 📊 Difficulty Target Metrics

| Level Range | Deaths/Level | Time/Level | Complexity |
|-------------|--------------|------------|------------|
| 1-3 (Tutorial) | 3-5 | 1-3 min | Low |
| 4-6 (Basic) | 5-10 | 3-5 min | Medium |
| 7-9 (Intermediate) | 10-15 | 5-8 min | High |
| 10-12 (Advanced) | 15-25 | 8-12 min | Very High |

---

## 🔊 Audio Categories

### Ambient
- Base drone (60 Hz, -30 dB)
- Harmonic layer (responds to safety/danger)

### SFX
- **Movement**: Soft footsteps, silent for Shade
- **Light**: Smooth push, crystal rotation
- **Feedback**: Danger shimmer, death collapse
- **UI**: Soft blip (navigate), gentle confirm (select)

### Mixing Priority
1. Gameplay feedback (danger, death)
2. Environmental audio (lights)
3. Ambient soundscape

---

## 💀 Death States

### Source Death
```
Cause: Touches shadow/pit/hazard
Animation: Desaturate → particle burst (warm)
Duration: 0.5s
```

### Shade Death
```
Cause: Touches light/exits bounds
Animation: Desaturate → particle burst (cool)
Duration: 0.5s
```

### Reset
```
Transition: 1s smooth rewind
Visual: Ghost trail to start
Audio: Reverse whoosh
```

---

## 🧩 Puzzle Design Patterns

### Pattern 1: The Gauntlet
Linear path, sequential challenges, skill building

### Pattern 2: The Hub
Central room, multiple sub-puzzles, non-linear

### Pattern 3: The Reversal
Forward journey ≠ return journey, memory test

### Pattern 4: The Transformation
Environment changes mid-puzzle, adaptation

### Pattern 5: The Synchronization
Multiple moving parts align, timing mastery

---

## 🎯 Tagline Options

**Primary**: "Where you stand determines where you cannot."

**Alternatives**:
- "One body, two fates, infinite shadows."
- "Control the light. Survive the darkness. Master both."

---

## 🛠️ Implementation Priority Order

**Phase 1**: Core mechanics (Source, Shade, single light, Level 1)  
**Phase 2**: Multi-light, rotation (Levels 2-3)  
**Phase 3**: Patrol Light (Levels 4-5)  
**Phase 4**: Prism (Levels 6-7)  
**Phase 5**: Inversion (Levels 8-9)  
**Phase 6**: Combined mechanics (Levels 10-12)  

---

## 🧠 Cognitive Load Layers

| Layer | Description | Introduced |
|-------|-------------|------------|
| **Spatial** | Where is Source? | Level 1 |
| **Projection** | Where is shadow? | Level 1 |
| **Dual-State** | Both safe? | Level 2 |
| **Temporal** | When to move? | Level 4 |
| **Inverse** | Rules reversed | Level 8 |

---

## 📐 Shadow Projection Formula

```
Shadow Position = Source Pos + (Source Pos - Light Pos) × Extension

Extension = Distance to Surface / Distance to Light
```

**Edge Cases**:
- Source on light = no shadow (instant death)
- Infinite extension = cap at max distance
- Multiple lights = multiple shadows (all must be safe)

---

## ✅ Pre-Launch Checklist (Critical)

- [ ] All 12 levels completable by external testers
- [ ] Consistent 60 FPS on target hardware
- [ ] Tutorial teaches core mechanics clearly
- [ ] Difficulty curve feels fair (data-verified)
- [ ] Death feedback is informative, not punishing
- [ ] UI is accessible (colorblind safe, scalable)
- [ ] All audio mixed and balanced
- [ ] Save system reliable
- [ ] No game-breaking bugs

---

## 🎓 Design Mantras

> **"Clarity over decoration"** - Every visual serves gameplay

> **"Simple rules, complex puzzles"** - Depth from constraint

> **"Death is learning"** - Failure is graceful feedback

> **"Both must survive"** - Unity through duality

---

## 📏 Standard Level Dimensions

```
Platform thickness: 2 units
Source size: 20 units tall × 10 units wide
Shade size: Same as Source (perspective match)
Light source: 6-unit diameter
Grid snap: 4-unit increments
```

---

## 🌟 Success Indicators

**Players say**: "Oh! I see it now!" (clarity)  
**Players feel**: Satisfied after solving (not frustrated)  
**Players do**: Return to improve times (replayability)  
**Reviews mention**: "Elegant", "clever", "beautiful simplicity"  

---

## 🔗 Document Links

- **Full Design**: [GAME_DESIGN_DOCUMENT.md](./GAME_DESIGN_DOCUMENT.md)
- **Mechanics Detail**: [MECHANICS_DEEP_DIVE.md](./MECHANICS_DEEP_DIVE.md)
- **Visual/Audio/Tech**: [VISUAL_DESIGN_IMPLEMENTATION.md](./VISUAL_DESIGN_IMPLEMENTATION.md)
- **Project Overview**: [README.md](./README.md)

---

## 💾 Save This!

Print this page or keep it open during development. Quick reference = faster iteration.

**Version**: 1.0  
**Last Updated**: November 10, 2025  
**Status**: Production-ready reference

---

**Remember**: Where you stand determines where you cannot. 🌓
