# 🎮 LEVEL 1 IMPLEMENTATION GUIDE - "The Basic Divide"

## Overview

This document provides a detailed, step-by-step implementation guide for **Level 1: The Basic Divide**, serving as a reference for implementing all subsequent levels.

---

## 📋 Level Specifications

### Objective
Teach the player:
1. Source must stay in light (shadow kills)
2. Shade must stay in darkness (light kills)
3. Shade position is determined by Source position
4. Shade can trigger environmental interactions

### Target Metrics
- **First-Time Completion**: 1-2 minutes
- **Expected Deaths**: 2-5
- **Par Time** (for speedrun): 15 seconds
- **Minimal Moves**: 8 position changes

---

## 🗺️ Level Layout (Grid-Based)

### Grid System
- **Unit Size**: 32 pixels
- **Grid Dimensions**: 30 units wide × 20 units tall
- **Origin**: Bottom-left corner (0, 0)

### ASCII Layout
```
20 ┌────────────────────────────────┐
19 │                                │
18 │         [OVERHEAD LIGHT]       │
17 │               │                │
16 │           ╱   │   ╲            │
15 │       ╱       │       ╲        │
14 │   ╱           │           ╲    │
13 │              ┌┴┐              │
12 │              │G│ [GOAL]        │
11 │══════════════╧═╧══════════════ │ ← Top Platform
10 │                                │
9  │          [GAP: 6 units]        │
8  │                                │
7  │══════════════   ══════════════ │ ← Mid Platform (broken)
6  │              │ │               │
5  │    ┌─(S)─┐   │ │               │ ← Source Start
4  │    └─────┘   │ │               │
3  │══════════════╧═╧══════════════ │ ← Ground Platform
2  │                                │
1  │                                │
0  └────────────────────────────────┘
   0         10        20        30

LOWER LEVEL (Shadow Projection):
-2 ══════════════════════════════════ ← Shadow Floor
-3             [Shade]
-4        ╔════════════╗
-5        ║ Laser Gate ║ ← Projects upward
-6        ╚════════════╝
-7 ══════════════════════════════════
```

### Coordinate Details

**Source Start Position**: (6, 5)  
**Goal Position**: (18, 12)  
**Overhead Light**: (15, 18)  
**Gap in Mid Platform**: X: 14-19 (6 units wide)  
**Laser Gate**: (12, -5) to (18, -5)  
**Shadow Floor**: Y: -2

---

## 🧩 Object List & Properties

### 1. Source (Player Character)

```javascript
{
  position: { x: 6, y: 5 },
  size: { width: 10, height: 20 }, // in pixels (0.31 × 0.625 units)
  speed: 4, // units per second
  jumpForce: 10, // upward velocity
  color: "#FFFFFF",
  glowColor: "#FFE5CC",
  glowOpacity: 0.05,
  collisionLayer: "player",
  safeIn: "light",
  diesIn: "shadow"
}
```

### 2. Shade (Shadow Character)

```javascript
{
  position: { x: 0, y: 0 }, // Calculated dynamically
  size: { width: 10, height: 20 }, // Matches Source
  color: "#000000",
  glowColor: "#CCE5FF",
  glowOpacity: 0.03,
  collisionLayer: "shadow",
  safeIn: "darkness",
  diesIn: "light",
  linkedTo: "Source", // Position calculated from Source + Light
  projectionPlane: "shadowFloor" // Y: -2
}
```

### 3. Overhead Light

```javascript
{
  type: "static-omnidirectional",
  position: { x: 15, y: 18 },
  radius: 12, // units (light reaches 12 units in all directions)
  intensity: 1.0,
  color: "#F5F5F5",
  castsShadows: true,
  animated: {
    pulse: true,
    pulsePeriod: 1.0, // seconds
    pulseAmount: 0.05 // ±5% brightness
  }
}
```

### 4. Platforms

```javascript
// Ground Platform
{
  type: "platform",
  position: { x: 0, y: 3 },
  size: { width: 30, height: 2 },
  color: "#808080",
  collidable: true,
  castsShadows: false
}

// Mid Platform (Left Section)
{
  type: "platform",
  position: { x: 0, y: 7 },
  size: { width: 14, height: 2 },
  color: "#808080",
  collidable: true,
  castsShadows: false
}

// Mid Platform (Right Section)
{
  type: "platform",
  position: { x: 20, y: 7 },
  size: { width: 10, height: 2 },
  color: "#808080",
  collidable: true,
  castsShadows: false
}

// Top Platform
{
  type: "platform",
  position: { x: 0, y: 11 },
  size: { width: 30, height: 2 },
  color: "#808080",
  collidable: true,
  castsShadows: false
}

// Shadow Floor (for Shade)
{
  type: "platform",
  position: { x: 0, y: -2 },
  size: { width: 30, height: 2 },
  color: "#1A1A1A",
  collidable: true, // Only for Shade
  castsShadows: false,
  layer: "shadowWorld"
}
```

### 5. Laser Gate

```javascript
{
  type: "laser-gate",
  position: { x: 12, y: -5 },
  size: { width: 6, height: 8 },
  direction: "upward", // Projects beam toward gap
  beamColor: "#FF6666",
  beamOpacity: 0.3,
  beamWidth: 0.5, // units
  state: "active", // "active" or "blocked"
  triggersWhen: "blocked",
  triggerAction: "spawnBridge"
}
```

### 6. Bridge (Dynamic Object)

```javascript
{
  type: "bridge",
  position: { x: 14, y: 7 }, // Spans the gap
  size: { width: 6, height: 2 },
  color: "#A0A0A0",
  collidable: false, // Initially
  visible: false, // Initially
  spawnAnimation: {
    type: "extend",
    duration: 0.5, // seconds
    easing: "ease-out"
  },
  triggeredBy: "laserGate"
}
```

### 7. Goal

```javascript
{
  type: "goal",
  position: { x: 18, y: 12 },
  size: { width: 3, height: 3 },
  color: "#CCFFE5",
  glowColor: "#00FF88",
  glowOpacity: 0.2,
  animated: {
    float: true,
    floatAmplitude: 0.5, // units
    floatPeriod: 2.0 // seconds
  },
  requiresBoth: true // Both Source and Shade must be in "completed" state
}
```

---

## ⚙️ Core Systems Implementation

### System 1: Shadow Projection Calculation

```javascript
function calculateShadePosition(source, light, shadowPlane) {
  // Vector from light to source
  const dx = source.x - light.x;
  const dy = source.y - light.y;
  
  // Calculate where shadow ray intersects shadow plane
  // Shadow plane is at y = -2
  const t = (shadowPlane.y - light.y) / dy;
  
  // Shade position
  const shadeX = light.x + (dx * t);
  const shadeY = shadowPlane.y + (source.height / 2); // On surface
  
  return { x: shadeX, y: shadeY };
}

// Example calculation:
// Light at (15, 18), Source at (6, 5), Shadow plane at y = -2
// dx = 6 - 15 = -9
// dy = 5 - 18 = -13
// t = (-2 - 18) / -13 = 20 / 13 ≈ 1.538
// shadeX = 15 + (-9 * 1.538) = 15 - 13.85 ≈ 1.15
// shadeY = -2 + 10 = -1 (on shadow floor)
```

### System 2: Light Zone Detection

```javascript
function isInLight(entity, lights) {
  for (let light of lights) {
    const distance = Math.sqrt(
      Math.pow(entity.x - light.x, 2) + 
      Math.pow(entity.y - light.y, 2)
    );
    
    if (distance <= light.radius) {
      return true; // Entity is in light
    }
  }
  return false; // Entity is in darkness
}
```

### System 3: Death Detection

```javascript
function checkDeathConditions(source, shade, lights) {
  const sourceInLight = isInLight(source, lights);
  const shadeInLight = isInLight(shade, lights);
  
  if (!sourceInLight) {
    return { dead: true, entity: "Source", reason: "in shadow" };
  }
  
  if (shadeInLight) {
    return { dead: true, entity: "Shade", reason: "in light" };
  }
  
  // Check for pit/void death
  if (source.y < 0 || source.y > 20) {
    return { dead: true, entity: "Source", reason: "out of bounds" };
  }
  
  return { dead: false };
}
```

### System 4: Laser Gate Trigger

```javascript
function updateLaserGate(laserGate, shade) {
  const shadeInBeam = checkCollision(shade, laserGate.beamHitbox);
  
  if (shadeInBeam) {
    laserGate.state = "blocked";
    triggerAction(laserGate.triggerAction); // Spawns bridge
  } else {
    laserGate.state = "active";
  }
}

function triggerAction(actionName) {
  if (actionName === "spawnBridge") {
    bridge.visible = true;
    bridge.collidable = false; // Start animation
    
    // Animate bridge extension
    animateBridge(bridge, 0.5, () => {
      bridge.collidable = true; // Collision enabled after animation
    });
  }
}
```

### System 5: Win Condition

```javascript
function checkWinCondition(source, goal) {
  const sourceAtGoal = checkCollision(source, goal);
  
  // In Level 1, only Source needs to reach goal
  // Shade's job is to enable the bridge
  if (sourceAtGoal) {
    return true;
  }
  
  return false;
}
```

---

## 🎬 Step-by-Step Walkthrough (Player Perspective)

### Initial State (t = 0:00)

**Source**: Standing on ground platform at (6, 5), illuminated by overhead light ✅  
**Shade**: Projected onto shadow floor at (~1, -1), in darkness ✅  
**Laser Gate**: Active, beam projecting upward through gap  
**Bridge**: Invisible, not spawned  
**Player Sees**: Character in light, shadow visible on lower level, gap ahead

**Tutorial Prompt** (if enabled): 
```
"Move forward. Stay in the light."
```

---

### Step 1: Initial Movement (t = 0:02)

**Player Input**: Press RIGHT (D key)  
**Source Action**: Moves right from (6, 5) → (10, 5)  
**Shade Action**: Automatically moves right on shadow floor (~1, -1) → (~4, -1)  
**Safety Check**: Source still in light ✅, Shade still in darkness ✅  

**Player Sees**: Character walking, shadow moving in parallel below

---

### Step 2: Approaching Laser (t = 0:05)

**Player Input**: Continue holding RIGHT  
**Source Position**: (12, 5)  
**Shade Position**: (~7, -1) — approaching laser gate zone  
**Laser Status**: Still active (Shade not blocking yet)  

**Player Sees**: Gap visible ahead, laser beam glowing upward through gap

**Tutorial Prompt** (if enabled):
```
"Your shadow can interact with objects."
```

---

### Step 3: Laser Interception (t = 0:07) — CRITICAL MOMENT

**Player Input**: Continue RIGHT  
**Source Position**: (14, 5)  
**Shade Position**: (~9, -1)  
**Laser Check**: Shade collides with laser beam hitbox!  

**Trigger Event**:
```javascript
laserGate.state = "blocked"
spawnBridge()
```

**Visual Feedback**:
- Laser beam changes color (red → green)
- Bridge begins extending animation (0.5s)
- Sound effect: Mechanical extension sound

**Player Sees**: Bridge appears across the gap! ✨

---

### Step 4: Crossing the Bridge (t = 0:10)

**Player Input**: Continue RIGHT, then JUMP to reach bridge  
**Source Position**: Moves onto bridge at (17, 7), then jumps to (17, 12)  
**Shade Position**: (~12, -1) — remains blocking laser  
**Bridge Status**: Fully extended, collidable  
**Safety Check**: Source in light ✅, Shade in darkness ✅  

**Player Sees**: Successfully crossing gap using newly-spawned bridge

---

### Step 5: Reaching Goal (t = 0:14)

**Player Input**: Move RIGHT toward goal  
**Source Position**: (18, 12)  
**Goal Collision**: Detected!  

**Win Condition**:
```javascript
checkWinCondition(source, goal) === true
```

**Victory Sequence**:
1. Goal object pulses bright green (0.3s)
2. Source and Shade fade to white particles (0.5s)
3. Level complete screen appears (1.0s)
4. Display stats: Time, Deaths, Moves

**Player Sees**: 
```
╔══════════════════════════════╗
║    LEVEL 1 COMPLETE!         ║
║                              ║
║    Time: 0:14                ║
║    Deaths: 0                 ║
║    Par Time: 0:15 ⭐         ║
║                              ║
║    [Continue to Level 2]     ║
╚══════════════════════════════╝
```

---

## 🐛 Common Player Mistakes & Safety Checks

### Mistake 1: Moving into Shadow Edge

**Scenario**: Player moves Source too far from light center  
**Detection**: `isInLight(source)` returns false  
**Response**: 
- Source border pulses red (warning, 2 Hz)
- If continues: Death triggered
- Death animation: 0.5s desaturation + particle burst
- Reset to start position after 1s

**Feedback**: Visual danger warning before death occurs

---

### Mistake 2: Approaching Gap Too Fast

**Scenario**: Player runs toward gap without bridge  
**Detection**: Source approaching X > 13 while bridge not spawned  
**Response**:
- No intervention (player should learn from failure)
- If Source falls into gap: Pit death
- If Shade hasn't reached laser yet, bridge won't spawn

**Learning**: Player must understand Shade triggers the bridge

---

### Mistake 3: Shade Enters Light (Shouldn't Happen in Level 1)

**Scenario**: Due to light radius, Shade theoretically could enter light  
**Detection**: `isInLight(shade)` returns true  
**Response**:
- Immediate death (Shade cannot survive in light)
- Show visual feedback: Shade location highlighted when death occurs

**Note**: Level 1 geometry prevents this, but system must handle it

---

## 📊 Telemetry & Analytics

### Events to Track

```javascript
// Track these events for difficulty tuning
analyticsEvents = [
  { event: "level_started", levelId: 1, timestamp: "2025-11-10T12:00:00Z" },
  { event: "source_moved", position: { x: 10, y: 5 }, timestamp: "..." },
  { event: "shade_entered_laser", timestamp: "..." },
  { event: "bridge_spawned", timestamp: "..." },
  { event: "source_death", cause: "in_shadow", timestamp: "..." },
  { event: "level_completed", time: 14, deaths: 0, timestamp: "..." }
]
```

### Metrics to Calculate

1. **Completion Rate**: % of players who complete vs start
2. **Average Time**: Mean completion time (target: 60-90 seconds first try)
3. **Death Rate**: Average deaths per completion (target: 2-5)
4. **Drop-Off Points**: Where do players quit? (heatmap of death locations)
5. **A/B Test Tutorial**: Prompts on vs off — which has better completion?

---

## 🎨 Visual Polish Checklist

- [ ] Source character has smooth walk animation (2-frame cycle)
- [ ] Shade silhouette perfectly matches Source shape
- [ ] Light source has subtle pulse animation
- [ ] Shadow projection line visible (helps player understand link)
- [ ] Laser gate beam has animated particles
- [ ] Bridge extension animation smooth (ease-out)
- [ ] Goal has gentle float animation
- [ ] Death particles disperse in direction of impact
- [ ] Reset transition shows ghost trail to start
- [ ] Background has subtle particle field (stars/dust)

---

## 🔊 Audio Event List

| Event | Sound | Volume | Priority |
|-------|-------|--------|----------|
| Source footstep | Soft tap | -20 dB | Low |
| Source jump | Whoosh up | -18 dB | Medium |
| Source land | Thump | -18 dB | Medium |
| Danger warning | Shimmer (2000 Hz) | -15 dB | High |
| Death | Harmonic collapse | -12 dB | Critical |
| Laser blocked | Mechanical click | -15 dB | Medium |
| Bridge spawn | Extension sound | -15 dB | High |
| Goal reached | Ascending arpeggio | -10 dB | Critical |
| Ambient drone | 60 Hz continuous | -30 dB | Constant |

---

## 🧪 Testing Checklist

### Functional Tests

- [ ] Source can move left/right on all platforms
- [ ] Source can jump (reaches bridge from ground)
- [ ] Source dies when entering shadow
- [ ] Shade position updates in real-time with Source movement
- [ ] Shade dies when entering light (test edge cases)
- [ ] Laser gate detects Shade collision correctly
- [ ] Bridge spawns when laser blocked
- [ ] Bridge collision works after animation completes
- [ ] Goal triggers win condition
- [ ] Reset returns all objects to initial state
- [ ] Death animation plays correctly
- [ ] Level complete screen displays stats

### Edge Cases

- [ ] Source directly under light (Shade vanishes — handle gracefully)
- [ ] Source jumps — Shade position updates mid-air
- [ ] Player dies during bridge animation — bridge resets
- [ ] Player reaches goal before bridge fully extends (shouldn't be possible)
- [ ] Rapid left-right movement — Shade follows smoothly
- [ ] Pause during animations — animations pause correctly

### Performance

- [ ] Maintains 60 FPS on target hardware
- [ ] Shadow projection calculated every frame without lag
- [ ] No memory leaks on repeated resets
- [ ] Level loads in < 0.5 seconds

---

## 🚀 Implementation Order (Recommended)

### Day 1: Core Systems
1. Setup scene with platforms
2. Implement Source controller (move, jump, collision)
3. Add single overhead light
4. Implement light zone detection

### Day 2: Shadow System
1. Add shadow floor (lower level)
2. Implement shadow projection calculation
3. Create Shade entity
4. Link Shade to Source movement
5. Test real-time shadow updates

### Day 3: Death & Safety
1. Implement death detection (Source in shadow, Shade in light)
2. Add death animation
3. Implement reset functionality
4. Add danger proximity warnings

### Day 4: Puzzle Mechanics
1. Add laser gate object
2. Implement Shade collision with laser
3. Create bridge object
4. Implement bridge spawn trigger
5. Add bridge extension animation

### Day 5: Goal & Completion
1. Add goal object
2. Implement win condition detection
3. Create level complete screen
4. Add stats tracking (time, deaths)

### Day 6: Polish
1. Add all animations (pulse, float, particles)
2. Implement all sound effects
3. Add tutorial prompts (optional)
4. Visual polish (glows, effects)

### Day 7: Testing & Iteration
1. Comprehensive playtesting
2. Difficulty tuning (adjust light radius, gap size, etc.)
3. Bug fixes
4. Performance optimization

---

## 🎓 Learning Outcomes (For Player)

By completing Level 1, the player should understand:

✅ **Rule 1**: Source must stay in light (shadow = death)  
✅ **Rule 2**: Shade must stay in darkness (light = death)  
✅ **Rule 3**: Shade's position is determined by Source + Light geometry  
✅ **Rule 4**: Shade can trigger environmental objects (buttons, gates)  
✅ **Mechanic**: Basic spatial reasoning (where will my shadow be?)  

**Player is now ready for**: Level 2 (rotational geometry)

---

## 📝 Developer Notes

### Why This Level Works

1. **Single Constraint**: Only one light source, simple geometry
2. **Clear Causality**: Player sees Shade block laser → bridge appears
3. **Forgiving**: Light radius is generous, hard to accidentally die
4. **Quick**: 15-second completion for skilled players (no frustration)
5. **Teaching**: Each element teaches exactly one concept

### Potential Issues

**Issue 1**: Players don't realize Shade triggers the bridge  
**Solution**: Add tutorial prompt "Your shadow can interact with objects" when approaching laser

**Issue 2**: Players move too fast and miss the laser interaction  
**Solution**: Make laser beam more visually prominent, add sound when Shade approaches

**Issue 3**: Shadow projection feels disconnected from Source  
**Solution**: Add visible line from Source to Shade, make Shade movement perfectly smooth

---

## 🔧 Tuning Parameters (For Balancing)

| Parameter | Default | Range | Effect |
|-----------|---------|-------|--------|
| Light Radius | 12 units | 10-15 | Smaller = harder |
| Gap Width | 6 units | 5-8 | Wider = more obvious bridge needed |
| Bridge Spawn Delay | 0.5s | 0.3-1.0s | Shorter = more responsive |
| Death Warning Time | 0.5s | 0.2-1.0s | Longer = more forgiving |
| Source Walk Speed | 4 u/s | 3-6 | Faster = harder to control |

**Recommended Tuning Session**: Have 5-10 playtesters complete, gather feedback, adjust parameters

---

## ✅ Completion Criteria

**Level 1 is complete when**:

- [ ] All systems functional (movement, shadow, death, trigger)
- [ ] Average first-time completion: 60-90 seconds
- [ ] Average deaths on first try: 2-5
- [ ] 80%+ playtester completion rate (high accessibility)
- [ ] No game-breaking bugs
- [ ] Visual polish complete (animations, effects)
- [ ] Audio implemented and balanced
- [ ] Tutorial prompts clear (if enabled)
- [ ] Win condition reliable (100% of goal collisions trigger)

---

**When Level 1 meets all criteria → Proceed to Level 2 implementation**

**Document Version**: 1.0  
**Created**: November 10, 2025  
**Status**: Complete Implementation Reference  
**Next Steps**: Use as template for Levels 2-12 implementation guides
