# 🔬 SHADE & SOURCE - Mechanics Deep Dive

## 🧩 PUZZLE DESIGN PHILOSOPHY

### The Core Tension
Every puzzle in Shade & Source exploits the fundamental paradox:
- **Unified Control**: Player controls ONE entity (Source)
- **Dual Survival**: TWO entities must survive (Source + Shade)
- **Opposite Requirements**: What's safe for one is deadly for the other
- **Linked Fate**: Both must reach goal state to complete level

This creates a unique cognitive load: **simultaneous opposite-state management**.

---

## 🎯 DETAILED MECHANIC BREAKDOWNS

### 🔸 Light Source Taxonomy

#### Type 1: Static Omnidirectional
- **Behavior**: Fixed position, radiates light in all directions
- **Shadow**: Creates single shadow of Source in opposite direction from light
- **Use Case**: Foundational puzzles, creates predictable shadow zones
- **Player Control**: None (environmental constant)

#### Type 2: Static Directional (Spotlight)
- **Behavior**: Fixed position, cone of light in one direction
- **Shadow**: Creates elongated shadow in beam direction
- **Use Case**: Precision puzzles requiring exact shadow placement
- **Player Control**: Some may be rotatable

#### Type 3: Moveable Light
- **Behavior**: Can be pushed/pulled by Source
- **Shadow**: Changes dynamically as light moves
- **Use Case**: Player-authored solutions, creative problem solving
- **Player Control**: Full positional control (within constraints)

#### Type 4: Patrol Light (New Mechanic)
- **Behavior**: Automated movement along fixed path
- **Shadow**: Continuously shifting shadow direction and length
- **Use Case**: Timing-based puzzles, rhythm challenges
- **Player Control**: Indirect (may have speed controls or pause switches)

#### Type 5: Prism-Split Light (New Mechanic)
- **Behavior**: Divides one light into multiple directional beams
- **Shadow**: Creates multiple simultaneous shadows of Source
- **Use Case**: Multi-constraint optimization puzzles
- **Player Control**: Rotation of prism changes all beam directions

---

## 🌑 SHADOW PROJECTION MATHEMATICS

### Basic Shadow Projection Formula

```
Shadow Position = Source Position + (Source Position - Light Position) × Extension Factor

Where Extension Factor = Distance to Shadow Surface / Distance to Light
```

### Multi-Plane Projection

When light hits Source at angle θ:
- **Floor Shadow**: Projects along floor plane (standard)
- **Wall Shadow**: Projects onto vertical plane (when light angle allows)
- **Ceiling Shadow**: Possible with uplighting (advanced mechanic)

### Edge Cases:
1. **Source directly on light**: No shadow (Shade ceases to exist = instant fail)
2. **Light parallel to surface**: Infinite shadow extension (handled with max distance cap)
3. **Multiple lights**: Multiple shadows = all must be in safe zones

---

## 💀 DEATH MECHANICS & FAIL STATES

### Source Death Conditions:
1. **Shadow Contact**: Source touches ANY shadow zone
2. **Pit/Void Contact**: Source falls into marked death zones
3. **Hazard Contact**: Source touches spikes, lasers (if present in level)

### Shade Death Conditions:
1. **Light Contact**: Shade touches ANY light zone
2. **Void Exit**: Shade projects beyond playable bounds
3. **Light Overlap**: Multiple light sources create zero-shadow zone where Shade exists

### Fail State Presentation:
- **Visual**: Instant desaturation + entity fade
- **Audio**: Subtle harmonic dissonance (not punishing)
- **Feedback**: Brief visual trace showing what killed which entity
- **Reset**: Smooth rewind to level start (1-second transition)

**Design Philosophy**: Death is a learning tool, not a punishment. Make it graceful.

---

## 🎮 ADVANCED MECHANICS - DEEP DIVE

### 🔷 MECHANIC: Patrol Light (Expanded)

#### Patrol Patterns:
1. **Linear Loop**: Back and forth on straight rail
2. **Circular**: Continuous rotation around central point
3. **Multi-Point**: Stops at waypoints before continuing
4. **Pendulum**: Swinging light with acceleration/deceleration

#### Timing Complexity Levels:

**Level 1 - Observable Rhythm**:
- Patrol cycle: 8 seconds
- Player has 4-second windows to act
- Single patrol light
- Clear visual indicator of light position

**Level 2 - Prediction Required**:
- Patrol cycle: 6 seconds
- Player must move during light transition
- Shadow path only safe for 2-second windows
- Requires memorization of cycle

**Level 3 - Multiple Patrol Coordination**:
- 2+ patrol lights with different cycle times
- Safe windows only when lights align specific ways
- Requires mathematical thinking (LCM of cycles)

**Level 4 - Interactive Speed Control**:
- Player can speed up/slow down patrol via lever
- Faster = riskier but quicker solution
- Slower = safer but tests patience
- Optimal solution requires specific speed settings

#### Puzzle Example: "The Pendulum Crossing"

```
                [Swinging Light]
                       ║
                   ╱       ╲
              ╱               ╲
         ╱                       ╲
    [Shadow]                  [Shadow]
      Zone                      Zone
        A                         B
        
═══════════════════════════════════════
[Start]         [Gap]            [Goal]
               (needs            
                bridge)

Solution:
- When light swings LEFT, Shade is in Zone B (safe)
- Shade in Zone B activates bridge mechanism
- Source must cross bridge when light swings RIGHT
  (Source in light, safe)
- Timing window: ~2 seconds
```

---

### 🔷 MECHANIC: Prism Splitter (Expanded)

#### Prism Types:

**Type A: Dual Splitter (45° angles)**
```
    Input
      │
      ▼
   [PRISM]
    ╱   ╲
   ╱     ╲
Beam A   Beam B

Creates 2 shadows at 90° from each other
```

**Type B: Triple Splitter (30° angles)**
```
    Input
      │
      ▼
   [PRISM]
   ╱ │ ╲
  ╱  │  ╲
 A   B   C

Creates 3 shadows at 60° intervals
```

**Type C: Focused Beam (no split, but intensifies/extends)**
```
Input → [PRISM] → Extended Beam

Creates single shadow but at greater distance
```

#### Rotation Mechanics:
- **90° Rotations**: Snap to cardinal directions (easier)
- **Free Rotation**: Any angle (advanced puzzles)
- **Locked Rotation**: Can only rotate between 2-3 preset angles

#### Multi-Shadow Management Puzzle: "The Triplet Paradox"

```
        [Triple Prism - Rotatable]
               ╱ │ ╲
              ╱  │  ╲
         [S₁] [S₂] [S₃]  ← Three Shade instances
         
Environment:
- [S₁] must press Button A (in shadow zone)
- [S₂] must avoid Laser Field (must be in darkness)
- [S₃] must avoid Wall Light (must be in darkness)

Source must position + Prism must rotate such that:
ALL THREE shadows are in safe darkness simultaneously

Solution requires geometric calculation:
- Rotate prism to 37° angle
- Position Source at coordinates (5, 3)
- This creates configuration where all constraints satisfied
```

---

### 🔷 MECHANIC: Inversion Field (Expanded)

#### Field Types:

**Type 1: Complete Inversion**
- Source: Light → Death, Shadow → Safe
- Shade: Shadow → Death, Light → Safe
- Visual: Purple/violet shimmer

**Type 2: Partial Inversion (Source Only)**
- Source rules invert
- Shade rules remain normal
- Visual: Red shimmer
- Use: Asymmetric puzzle solving

**Type 3: Partial Inversion (Shade Only)**
- Shade rules invert
- Source rules remain normal
- Visual: Blue shimmer
- Use: Shadow-focused challenges

**Type 4: Delayed Inversion**
- 3-second delay after entering before inversion takes effect
- Creates timing-based transition puzzles
- Visual: Pulsing boundary

#### Cognitive Challenge Design:

**First Inversion Level: "The Threshold"**
```
[Normal]  ║ [INVERTED] ║  [Normal]
          ║            ║
[Light]   ║  [Shadow]  ║  [Light]
Source    ║   Source   ║  Source
HERE      ║   must     ║  GOAL
(safe)    ║   be here  ║  (safe)
          ║  (inverted)║
          
Problem: Source must cross inversion boundary
- Start in normal light (safe)
- Must enter inversion field INTO SHADOW (now safe in inversion)
- Must exit inversion field INTO LIGHT (safe again in normal)

Requires finding shadow zones AT THE BOUNDARY
```

#### Advanced Inversion Puzzle: "Dual Phase Shift"

Two inversion fields, overlapping:
- Field A: Inverts Source only
- Field B: Inverts Shade only
- Overlap Zone: Both inverted (returns to "normal" ruleset!)

```
       [Field A]
          │
          ├────[Overlap]────┤
          │    [Field B]    │
          │                 │
          
In Overlap: Double inversion = normal rules
Creates safe "island" of normalcy within inverted zones
```

---

## 🧠 COGNITIVE LOAD ANALYSIS

### Player Mental Models:

#### Model 1: Spatial Awareness (Low Load)
- "Where is my Source?"
- "Where is the light?"
- Single-entity tracking

#### Model 2: Shadow Projection (Medium Load)
- "Where will my shadow be?"
- "What happens if I move here?"
- Requires geometric intuition

#### Model 3: Dual-State Management (High Load)
- "Is Source safe AND is Shade safe?"
- "What move keeps BOTH alive?"
- Requires simultaneous constraint checking

#### Model 4: Temporal Prediction (Very High Load)
- "Where will patrol light be in 3 seconds?"
- "When is the safe window to move?"
- Requires forward simulation

#### Model 5: Inverse Logic (Extreme Load)
- "In inversion zone, light kills Source..."
- "Wait, so I need to find shadow..."
- Requires mental model reversal

### Progressive Load Curve:
```
Levels 1-3:   Models 1-2 (Spatial + Shadow)
Levels 4-6:   Models 1-3 (Add Dual-State)
Levels 7-9:   Models 1-4 (Add Temporal)
Levels 10-12: Models 1-5 (Add Inverse)
```

---

## 🎨 AESTHETIC MECHANICS

### Visual Feedback Systems:

#### Safe Zone Indicators:
- **For Source**: Very subtle warm glow on light edges (barely visible)
- **For Shade**: Very subtle cool glow on shadow edges
- **Neutral Zones**: Pure greyscale

#### Danger Proximity Warning:
- **Approaching Death Zone**: Entity outline begins to shimmer/pulse
- **Critical Distance** (0.5 units): Pulse accelerates
- **Contact**: Instant desaturation + fade

#### Light Quality:
- **Natural Light**: Soft edges, warm undertone
- **Artificial Light**: Hard edges, neutral/cool tone
- **Hazard Light**: Sharp edges, slight red tint
- **Inversion Field**: Purple/violet internal glow

### Audio Design:

#### Ambient Layer:
- Minimal drone (neutral tone)
- Subtle harmonic shifts based on entity positions
- Safe zones = consonant harmonics
- Danger proximity = slight dissonance

#### Interaction Audio:
- Light source movement: Smooth tone glide
- Prism rotation: Crystalline chime
- Switch activation: Soft mechanical click
- Death: Harmonic collapse (not jarring)

#### Musical Structure:
- No melody (too distracting)
- Generative harmony based on game state
- Tension builds through harmonic density
- Completion = resolution to tonic

---

## 🏆 MASTERY & REPLAYABILITY

### Challenge Modes:

#### Speed Run Mode:
- Timer displayed
- Leaderboards for each level
- Par times for Bronze/Silver/Gold

#### Minimal Moves:
- Count every position change
- Optimize for fewest movements
- Puzzle becomes efficiency challenge

#### No Reset:
- Cannot die or must restart entire game
- For mastery players only
- Unlocks after completing all levels

#### Inverse Challenge:
- All levels have inversion field variants
- Familiar puzzles become completely different
- Requires relearning solutions

### Accessibility Options:

#### Visual Aids:
- **Shadow Path Preview**: Show where shadow will land (toggle)
- **Safe Zone Highlight**: Increase visibility of safe zones
- **Slow Motion**: Reduce patrol light speeds by 50%

#### Gameplay Aids:
- **Infinite Lives**: Remove death penalty (for learning)
- **Hint System**: Show general solution direction
- **Skip Level**: For stuck players (limits progression rewards)

---

## 🔮 ADVANCED CONCEPTS (Expansion Ideas)

### Mechanic: Mirror Surfaces
- Reflects light at 90° angles
- Creates secondary light sources
- Allows for "light around corners" puzzles

### Mechanic: Color Theory
- RGB light sources create colored shadows
- Mixing lights creates new shadow colors
- Some zones only accept specific shadow colors

### Mechanic: Time Dilation Zones
- Slow-time zones (easier patrol light navigation)
- Fast-time zones (Source moves quickly, requires precision)
- Time stops for one entity but not the other

### Mechanic: Gravity Inversion
- Some zones have reversed gravity
- Shadow projects upward instead of downward
- Creates ceiling-walking sequences

### Mechanic: Shadow Cloning
- Leave a "shadow clone" at a position
- Clone persists and can press buttons
- Creates multi-step sequence puzzles

---

## 📐 LEVEL DESIGN PATTERNS

### Pattern 1: The Gauntlet
- Linear path with sequential challenges
- Each section tests one specific skill
- Builds confidence through repetition

### Pattern 2: The Hub
- Central room connects to multiple sub-puzzles
- Each sub-puzzle rewards a key/unlock
- Non-linear, player chooses order

### Pattern 3: The Reversal
- Puzzle where you must "undo" what you did
- Return journey is different than forward
- Tests memory and inverse thinking

### Pattern 4: The Transformation
- Environment changes mid-puzzle
- What was safe becomes dangerous
- Adaptation challenge

### Pattern 5: The Synchronization
- Multiple moving parts must align
- Requires understanding of system timing
- Peak of mastery gameplay

---

## 🎓 EDUCATIONAL VALUE

### Skills Developed:

1. **Spatial Reasoning**: Understanding 3D projection onto 2D planes
2. **Logical Thinking**: If-then consequence chains
3. **Pattern Recognition**: Identifying safe/unsafe zones
4. **Problem Decomposition**: Breaking complex puzzles into steps
5. **Constraint Satisfaction**: Managing multiple simultaneous requirements
6. **Temporal Reasoning**: Predicting future states
7. **Inverse Reasoning**: Working backwards from goal

### Potential Educational Applications:
- Geometry teaching tool (light, shadow, angles)
- Logic puzzle supplement for schools
- Cognitive training for spatial reasoning
- Design thinking examples (constraint-based creativity)

---

*End of Mechanics Deep Dive*

**Document Version**: 1.0  
**Created**: November 10, 2025  
**Companion to**: GAME_DESIGN_DOCUMENT.md  
**Status**: Comprehensive Mechanics Reference
