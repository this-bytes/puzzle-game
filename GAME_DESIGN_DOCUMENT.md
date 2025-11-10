# 🌓 SHADE & SOURCE - Game Design Document

## 🎮 Game Title Analysis & Recommendations

### Original Titles:
- **Shade & Source** - Clean, alliterative, clearly communicates the dual nature
- **UmbraBound** - More poetic, mysterious, emphasizes constraint ("bound")

### AI-Generated Alternative Titles:
1. **Penumbra Protocol** - Emphasizes the puzzle/systematic nature
2. **Luminous Divide** - Poetic, emphasizes the light/dark separation
3. **Twinlight** - Portmanteau of "twin" + "light", suggests duality
4. **Threshold** - Simple, powerful, suggests the boundary between states
5. **Dual Lumen** - Latin feel, technical but elegant

**RECOMMENDATION**: **Shade & Source** - Most accessible while maintaining elegance. Clear thematic communication.

---

## 📜 TAGLINE

**"Where you stand determines where you cannot."**

*Alternative taglines:*
- "One body, two fates, infinite shadows."
- "Control the light. Survive the darkness. Master both."
- "In the space between light and shadow, neither can exist."

---

## 🗺️ DETAILED LEVEL ELABORATIONS

### 🔷 LEVEL 1: The Basic Divide
**Tutorial Level - Learning Core Survival Constraints**

#### Environment Layout:
```
[START]──(Source)                    [GOAL]
   │                                    │
   └─Light────┐                        │
              │                        │
   ═══════════╪════[GAP]═══════════════╧═══
              │         
   [Shadow]   │         [Platform appears when
   (Shade)    │          Shade blocks laser]
              │
   ═══════════╧═══════════════════════════
              └─Laser Gate (projects upward)
```

#### Specific Mechanics:
- **Starting Position**: Source stands in a pool of overhead light (safe zone)
- **Obstacle**: 3-unit gap in the floor ahead (Source cannot jump this distance)
- **Shadow Mechanism**: The Source's shadow projects downward onto a lower level
- **Laser Gate**: A horizontal laser beam projects upward through the gap
- **Critical Mechanic**: When the Shade (shadow) blocks the laser gate by moving into the beam's path, a bridge platform materializes across the gap

#### Solution Path:
1. **Initial State**: Source in light, Shade projected onto lower floor (safe in darkness)
2. **Player Action**: Move Source forward (right) while staying in light
3. **Automatic Result**: Shade moves right on lower floor
4. **Critical Moment**: Shade intersects with laser beam (still safe - laser is "darkness" for purposes of Shade)
5. **Trigger**: Laser gate blocked → Bridge extends across gap
6. **Completion**: Source walks across bridge to goal platform

#### Learning Objective:
- Source must stay in light (avoid shadow areas)
- Shade must stay in darkness (avoid light sources)
- Shade position is locked to Source position relative to light source
- Environmental interactions can be triggered by Shade positioning

---

### 🔶 LEVEL 2: Rotational Geometry
**Intermediate Level - Multi-Plane Shadow Projection**

#### Environment Layout:
```
              [Rotatable Light Source] ← Player can rotate 360°
                        │
                    ╱   │   ╲
               ╱        │        ╲
          ╱             │             ╲
[WALL]                  │                  [WALL]
  │                     │                     │
  │  ┌─Climbable────┐   │   ┌─────────┐      │
  │  │  Surface     │   │   │ Lethal  │      │
  │  │  (Dark OK)   │   │   │ Light   │      │
  │  └──────────────┘   │   └─────────┘      │
  │                     │                     │
══╧═════════════════════╧═════════════════════╧══
  [Start]             (Source)            [Goal]
                    (Platform)
```

#### Specific Mechanics:
- **Rotatable Light**: Ceiling-mounted light can be rotated 180° (from straight down to 45° angles)
- **Multi-Surface Projection**: Rotating the light changes whether the Source's shadow projects onto the floor OR the wall
- **Climbing Wall**: Left wall has climbable surface markers (only accessible to Shade in shadow form)
- **Goal Positioning**: Exit is on an elevated platform (requires wall climb)
- **Death Zones**: 
  - Floor sections with additional floor lights (Source safe, Shade dies)
  - Wall sections with wall-mounted lights (Shade safe, Source dies if shadow touches)

#### Solution Path:
1. **Initial State**: Light points straight down, Source on floor platform (lit), Shade projects downward (on dark floor - safe)
2. **Player Interaction**: Activate light rotation mechanism (lever/button near start)
3. **Rotation Phase 1**: Rotate light 30° to the left
   - Source remains on lit platform (safe)
   - Shade projection begins to shift from floor to left wall
4. **Movement Phase**: Move Source slightly left and forward
5. **Rotation Phase 2**: Continue rotating to 45° left angle
   - Shade now fully projects onto left wall's climbable surface (dark - safe)
   - Source still on platform in light cone (safe)
6. **Critical Geometry**: The light angle creates a shadow on the wall that forms a "path" upward
7. **Ascent**: As Source moves along the floor platform (staying in light), Shade "climbs" the wall shadow path
8. **Final Position**: Source reaches a floor switch, Shade reaches top of wall (where exit door is)
9. **Completion**: Shade's position at wall-top triggers door mechanism, both entities enter goal state

#### Learning Objective:
- Light angle dramatically changes shadow projection surfaces
- One entity can move horizontally while the other moves vertically
- Precise light positioning is critical for safe navigation
- Environmental geometry (walls, floors, ceilings) are all potential shadow surfaces

---

### 🔷 LEVEL 3: Interacting Shadows
**Advanced Level - Multiple Light Sources & Environmental Shadows**

#### Environment Layout:
```
[Static Light A]           [Moveable Lamp] ← Player can push/pull
        │                         │
        ▼                         ▼
    ┌───────┐                 ┌─────┐
    │ Block │                 │Light│
    │(casts │                 │Pool │
    │shadow)│                 └─────┘
    └───────┘                     │
        │                         │
    [Shadow A]                    │
══════╬═════════════╬══════════════╧═══════
      │         [Gap]              │
   (Shade)      [Pit]          (Source)
   needs        Death           needs
   this         Zone            this
   shadow!                      light!
      │                             │
      ▼                             ▼
   [Button A]────────→────────[Door/Goal]
```

#### Specific Mechanics:
- **Static Light A**: Ceiling-mounted, immovable, illuminates a large cube/block
- **Block Shadow**: Creates a rectangular shadow zone on the floor (safe for Shade)
- **Moveable Lamp**: Floor-based lamp that can be pushed/pulled by the Source
- **Gap/Pit**: Central death zone (kills both Source and Shade if either enters)
- **Dual Requirements**:
  - Shade must reach Button A (located in Block's shadow)
  - Source must reach the Goal (requires crossing the pit via a bridge that appears when Button A is pressed)
- **Complex Constraint**: Moving the lamp changes both:
  - Where Source can safely walk (light pools)
  - Where Shade projects (shadow of Source from lamp)

#### Solution Path:
1. **Initial State**: 
   - Source starts in moveable lamp's light pool (safe)
   - Shade projects behind Source (in darkness between two light sources - safe)
   - Block's shadow (Shadow A) is on the LEFT side of the block

2. **Analysis Phase**: Player must recognize:
   - Block's shadow is cast by Static Light A (unchangeable)
   - To get Shade to Button A, Source must position so Shade projects into Block's shadow
   - Source needs lamp light to cross the pit (once bridge appears)

3. **Step 1 - Shadow Navigation**:
   - Push moveable lamp TOWARD the static block
   - This creates a light corridor for Source to walk through
   - While pushing, Source moves LEFT (toward block)

4. **Step 2 - Critical Positioning**:
   - Position Source in the light pool created by moveable lamp
   - Ensure Source is positioned so Static Light A casts Source's shadow INTO the existing Block shadow
   - **Key Insight**: The Shade is now in Block's shadow (safe darkness), NOT in lamp light

5. **Step 3 - Button Activation**:
   - Fine-tune Source position until Shade overlaps with Button A location
   - Button A triggers → Bridge extends across pit

6. **Step 4 - Final Crossing**:
   - Pull moveable lamp BACK toward start position
   - This creates a light path across the newly-appeared bridge
   - Source walks across bridge in lamp light (safe)
   - Shade projects behind/beside Source (into void/darkness - safe)

7. **Completion**: Source reaches goal door

#### Advanced Learning Objectives:
- Multiple light sources create overlapping shadow/light zones
- Environmental objects (blocks) cast their own shadows (safe zones for Shade)
- Source's shadow and environmental shadows are DIFFERENT and can be used strategically
- Moveable light sources require planning multiple steps ahead
- Sometimes you must use one entity's required zone (darkness for Shade) that's created by a different mechanism (block shadow vs Source shadow)

---

## 💡 THREE ADDITIONAL LIGHT MANIPULATION MECHANICS

### 🔸 Mechanic 1: The Patrol Light (Automated Movement)
**Concept**: A light source that automatically moves along a fixed rail/path in a loop.

#### Implementation Details:
- **Visual**: Ceiling-mounted spotlight on a visible rail track
- **Behavior**: Moves at constant speed, reverses direction at endpoints
- **Puzzle Application**: Creates moving zones of safety/danger
- **Shadow Effect**: Source's shadow continuously shifts position and direction

#### Example Puzzle Usage:
```
[Rail Track]
════●═════════●═════════●════ (Light moves between points)
    ↓         ↓         ↓
  [Safe]   [Danger]  [Safe]   (zones shift as light moves)
  
  Player must TIME movement to match light patrol cycle
  Source moves during "safe light" phase
  Shade navigates during "safe shadow" phase
```

#### Strategic Depth:
- **Timing Challenges**: Player must wait for the right moment
- **Rhythm Gameplay**: Creates a tempo to puzzle solving
- **Prediction**: Player must visualize where shadows will be in future light positions
- **Speed Variations**: Later levels could have multiple patrol lights at different speeds

#### Advanced Variant:
- **Player-Controlled Speed**: A dial that changes patrol light speed (faster = more dangerous but quicker solutions)

---

### 🔸 Mechanic 2: The Prism Splitter (Light Division)
**Concept**: A prism object that splits one light source into multiple directional beams.

#### Implementation Details:
- **Visual**: Crystal/glass prism (geometric, minimalist)
- **Behavior**: Takes one input light beam, outputs 2-3 directional beams at angles
- **Interaction**: Can be rotated to change output beam directions
- **Shadow Effect**: Creates multiple shadows of the Source from a single original light

#### Example Puzzle Usage:
```
    [Single Light Source]
            │
            ▼
        [PRISM] ← Rotatable
        ╱  │  ╲
      ╱    │    ╲
  Beam A  Beam B  Beam C

  Each beam casts its own shadow of the Source
  Creates 3 Shades simultaneously
  ALL Shades must be in safe darkness to survive
```

#### Strategic Depth:
- **Multi-Constraint Solving**: Player must ensure ALL projected shadows are safe
- **Geometric Complexity**: Rotating prism changes ALL shadow positions at once
- **Combo Puzzles**: Some beams might need to hit specific targets while shadows avoid danger zones
- **Reflection Chains**: Prisms could chain (one prism's output feeds into another)

#### Advanced Variant:
- **Color Prisms**: Different colored light beams affect Shade differently (e.g., red light creates "slow" shadow, blue creates "fast" shadow)

---

### 🔸 Mechanic 3: The Inversion Field (Constraint Reversal)
**Concept**: A special zone where Source/Shade survival rules are temporarily reversed.

#### Implementation Details:
- **Visual**: Shimmering boundary/field with distinct visual effect (subtle color shift to violet/inverted palette)
- **Behavior**: Upon entering the field:
  - Source can ONLY exist in shadow (light kills Source)
  - Shade can ONLY exist in light (darkness kills Shade)
- **Interaction**: Cannot be moved, but can be activated/deactivated via switches
- **Shadow Effect**: Completely inverts player's mental model

#### Example Puzzle Usage:
```
[Normal Zone]  ║  [Inversion Field]  ║  [Normal Zone]
               ║                     ║
Source in      ║  Source in         ║  Source in
LIGHT = Safe   ║  SHADOW = Safe     ║  LIGHT = Safe
               ║                     ║
Shade in       ║  Shade in          ║  Shade in
SHADOW = Safe  ║  LIGHT = Safe      ║  SHADOW = Safe
               ║                     ║

Player must navigate Source from left → through field → to right
Requires complete mental model flip mid-puzzle
```

#### Strategic Depth:
- **Cognitive Challenge**: Forces player to reverse their learned instincts
- **Transition Zones**: The boundary between normal/inverted becomes critical
- **Partial Inversions**: Could have fields that only invert ONE entity (just Source OR just Shade)
- **Timed Inversions**: Fields that toggle on/off on a timer

#### Advanced Variant:
- **Inversion Propagation**: Entering an inversion field while holding/pushing an object causes that object to also invert (light-casting objects become shadow-casting)

---

## 🎯 MECHANICS SUMMARY TABLE

| Mechanic | Complexity | Primary Challenge | Cognitive Load |
|----------|-----------|------------------|----------------|
| **Patrol Light** | Medium | Timing & Prediction | Moderate - Temporal reasoning |
| **Prism Splitter** | High | Multi-Shadow Management | High - Spatial + Geometric |
| **Inversion Field** | Very High | Mental Model Reversal | Very High - Conceptual inversion |

---

## 🎨 PROGRESSIVE DIFFICULTY CURVE

### Tutorial Arc (Levels 1-3):
1. Basic Divide → Single constraint introduction
2. Rotational Geometry → Multi-plane thinking
3. Interacting Shadows → Multiple light sources

### Intermediate Arc (Levels 4-8):
4. First Patrol Light level (timing)
5. Combined Patrol + Rotation (timing + geometry)
6. First Prism level (multi-shadow)
7. Prism + Environmental shadows (complexity spike)
8. Multi-Prism spatial puzzle

### Advanced Arc (Levels 9-12):
9. First Inversion Field (cognitive reset)
10. Inversion + Patrol (reversed timing)
11. Inversion + Prism (reversed multi-constraint)
12. **Final Level**: All mechanics combined - "The Convergence"

---

## 🌟 NARRATIVE & THEMATIC DEPTH (Optional Layer)

### Minimalist Narrative Concept:
The Source and Shade were once unified. A mysterious event split them across the boundary of light and darkness. Each level represents a fragment of memory, a puzzle-space where they must cooperate despite existing in mutually exclusive states. The goal is reunification.

### Environmental Storytelling:
- Early levels: Simple geometric shapes (pure puzzle)
- Mid levels: Hints of architecture (abandoned spaces)
- Late levels: Recognizable locations (a room, a corridor, a door)
- Final level: The two entities occupy the same space simultaneously (impossible geometry that represents reunification)

### Thematic Resonance:
- **Duality**: Light/Dark, Source/Shade, Existence/Non-existence
- **Interdependence**: Neither can succeed without the other
- **Constraint as Freedom**: Limitations create possibility
- **Unity through Division**: Being split allows cooperation in impossible ways

---

## 📊 TECHNICAL CONSIDERATIONS (for Implementation)

### Core Systems Needed:
1. **Light Raycasting Engine**: Calculate light volumes and shadow projections in real-time
2. **Shadow Projection System**: Map Source position → Shade position based on light angles
3. **Collision Detection**: Separate layers for Source (light/shadow zones) and Shade (light/shadow zones)
4. **State Management**: Track which zones are safe/deadly for each entity
5. **Object Interaction**: Pushing/pulling/rotating light sources and prisms

### Visual Clarity Requirements:
- **High Contrast**: Stark black/white/grey palette
- **Clear Zone Marking**: Subtle visual indicators for safe/deadly zones
- **Shadow Definition**: Crisp shadow edges (no soft/ambient shadows that create ambiguity)
- **Light Source Visibility**: All light sources clearly visible and distinct
- **Feedback Systems**: Immediate visual feedback when approaching danger zones (subtle pulse/shimmer)

---

## 🎬 TAGLINE - FINAL RECOMMENDATION

### **Primary Tagline:**
## "Where you stand determines where you cannot."

**Why this works:**
- ✅ Paradoxical (intriguing)
- ✅ Directly references core mechanic (position-based constraint)
- ✅ Philosophical depth (echoes themes of choice and consequence)
- ✅ Memorable and quotable
- ✅ Works for marketing (mysterious but clear)

---

## 🚀 NEXT STEPS FOR DEVELOPMENT

1. **Prototype Level 1** in game engine to validate core mechanic feel
2. **Test shadow projection** mathematics for accuracy and player readability
3. **Iterate on visual style** - find the perfect balance of minimalism and clarity
4. **Playtest timing** on Patrol Light mechanic - find the "feels fair" speed
5. **Design full 12-level campaign** with difficulty curve mapping
6. **Compose ambient soundtrack** - minimal, meditative, tension-building
7. **Develop death/reset animation** - make failure feel like part of the aesthetic, not frustrating

---

*End of Game Design Document*

**Document Version**: 1.0  
**Created**: November 10, 2025  
**AI Design Lead**: Claude (Transcendent Creative Mode)  
**Status**: Ready for Prototyping
