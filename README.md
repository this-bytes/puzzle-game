# 🌓 Shade & Source - Project README

## Overview

**Shade & Source** is a minimalist 2D puzzle platformer where you simultaneously control a character (Source) and their shadow (Shade). Survive by manipulating light sources—the Source can only exist in light, while the Shade can only exist in darkness.

**Tagline**: *"Where you stand determines where you cannot."*

---

## 📚 Documentation Structure

This repository contains comprehensive game design documentation:

1. **[GAME_DESIGN_DOCUMENT.md](./GAME_DESIGN_DOCUMENT.md)** - Core game design, level concepts, mechanics, and taglines
2. **[MECHANICS_DEEP_DIVE.md](./MECHANICS_DEEP_DIVE.md)** - Detailed mechanics analysis, cognitive load, puzzle patterns
3. **[VISUAL_DESIGN_IMPLEMENTATION.md](./VISUAL_DESIGN_IMPLEMENTATION.md)** - Visual style, UI/UX, audio design, implementation roadmap
4. **[QUICK_REFERENCE.md](./QUICK_REFERENCE.md)** - Condensed cheat sheet for rapid reference

---

## 🎮 Core Concept

### Dual-State Survival Constraint
- **Source** (character): Dies in shadow, survives in light
- **Shade** (shadow): Dies in light, survives in shadow
- **Linked Movement**: Shade's position is determined by Source's position relative to light sources
- **Win Condition**: Both entities must reach the goal state

### Primary Mechanic
**Light Manipulation**: Move, rotate, or activate light sources to change shadow patterns, creating safe paths for both entities simultaneously.

---

## 🗺️ Three Core Level Concepts (Elaborated)

### Level 1: The Basic Divide
**Teaches**: Core survival constraints and linked movement

**Setup**: Source must cross a gap in the floor. A laser gate projects upward through the gap.

**Solution**: 
1. Move Source forward in light (safe)
2. Source's shadow (Shade) moves along lower floor (safe in darkness)
3. When Shade blocks the laser gate, a bridge materializes
4. Source crosses the bridge to reach the goal

**Learning**: Shade can trigger environmental interactions through positioning.

---

### Level 2: Rotational Geometry
**Teaches**: Multi-plane shadow projection

**Setup**: A rotatable ceiling light can project shadows onto floor OR walls. Goal requires vertical ascent.

**Solution**:
1. Rotate light source from straight down to 45° angle
2. Source moves along floor platform (staying in light cone)
3. As light angle changes, Shade projects onto wall instead of floor
4. Shade "climbs" the wall shadow path while Source walks horizontally
5. Precise light angle creates shadow path to elevated exit

**Learning**: Light angle dramatically changes which surface receives the shadow.

---

### Level 3: Interacting Shadows
**Teaches**: Multiple light sources and environmental shadows

**Setup**: Static light illuminates a block (creating block shadow). Moveable lamp provides Source's light. Gap requires bridge activation.

**Solution**:
1. Push moveable lamp toward static block
2. Position Source so Static Light casts Source's shadow INTO block's existing shadow
3. Shade (now in block's shadow) reaches Button A
4. Button activates bridge across gap
5. Pull lamp back to create light path across new bridge
6. Source crosses to goal

**Learning**: Environmental shadows (block) and Source's shadow are different strategic resources.

---

## 💡 Three Additional Light Mechanics

### 1. Patrol Light (Automated Movement)
- **Concept**: Light moves automatically along a fixed rail/path
- **Challenge**: Creates moving zones of safety/danger requiring timing
- **Variation**: Player-controlled speed dials, multiple patrol lights with different cycle times

**Example Puzzle**: Swinging pendulum light creates alternating safe zones—player must time crossing when light position allows both Source and Shade to be safe.

---

### 2. Prism Splitter (Light Division)
- **Concept**: Prism splits one light beam into 2-3 directional beams
- **Challenge**: Creates multiple shadows of Source—ALL must be in safe darkness
- **Variation**: Rotatable prisms change all beam angles simultaneously

**Example Puzzle**: Triple prism creates three shadows. Player must position Source + rotate prism so all three shadows avoid light zones while Source remains in light.

---

### 3. Inversion Field (Constraint Reversal)
- **Concept**: Special zones where survival rules flip (Source needs shadow, Shade needs light)
- **Challenge**: Complete mental model reversal mid-puzzle
- **Variation**: Partial inversions (only one entity inverts), timed inversions, overlapping fields

**Example Puzzle**: Navigate from normal zone → through inversion field → back to normal zone. Requires finding shadow AT the boundary to enter inverted zone safely.

---

## 🎯 Suggested Taglines

### Primary (Recommended):
**"Where you stand determines where you cannot."**
- Paradoxical and intriguing
- Directly references core mechanic
- Philosophical depth

### Alternatives:
- "One body, two fates, infinite shadows."
- "Control the light. Survive the darkness. Master both."
- "In the space between light and shadow, neither can exist."

---

## 🎨 Visual Style

- **Aesthetic**: Extreme minimalism, high-contrast black and white
- **Color Palette**: Grayscale primary, subtle warm/cool accents (5-10% opacity)
- **Character Design**: Abstract geometric humanoids (circle head, simple body)
- **Environment**: Geometric platforms, angular architecture, stark voids
- **Tone**: Meditative, intellectually challenging, visually striking

---

## 🏗️ Implementation Roadmap Summary

### Phase 1: Core Prototype (Weeks 1-4)
- Basic character controller, single light source, shadow projection
- Level 1 implementation
- Death detection and reset functionality

### Phase 2: Advanced Mechanics (Weeks 5-8)
- Multi-plane projection, rotatable lights
- Multiple light sources
- Levels 2-3 + Patrol Light mechanic

### Phase 3: Advanced Systems (Weeks 9-12)
- Prism Splitter, Inversion Field
- Visual polish, audio implementation
- UI/UX completion

### Phase 4: Content & Testing (Weeks 13-16)
- Full 12-level suite
- Comprehensive testing and balancing
- Marketing preparation

### Phase 5: Post-Launch
- Community engagement, patches
- DLC/expansion planning
- Mobile port consideration

---

## 🛠️ Recommended Technology

**Engine**: Godot (free, excellent 2D) or Unity (robust, cross-platform)

**Art**: Inkscape/Illustrator (vector graphics), Aseprite (sprites)

**Audio**: Audacity (sound design), LMMS (music composition)

**Version Control**: Git + GitHub

---

## 🎯 Target Audience

- Puzzle game enthusiasts (Portal, Braid, Limbo fans)
- Ages 18-35
- Platforms: PC (Steam), potentially mobile
- Values clever mechanics over graphics, intellectual challenge

---

## 📊 Success Metrics

- **Engagement**: 20-30 min average session, >70% completion rate for early levels
- **Difficulty**: 5-10 deaths for tutorial levels, 10-20 for advanced
- **Quality**: <0.1% crash rate, consistent 60 FPS
- **Business**: >4.0/5.0 review score, <5% refund rate

---

## 🌟 Educational Value

**Skills Developed**:
- Spatial reasoning (3D → 2D projection)
- Logical thinking (if-then consequence chains)
- Constraint satisfaction (multiple simultaneous requirements)
- Temporal reasoning (predicting future states)
- Inverse reasoning (working backwards from goals)

**Potential Applications**:
- Geometry teaching tool
- Logic puzzle supplement for education
- Cognitive training for spatial reasoning

---

## 📖 How to Use This Documentation

1. **Game Designers**: Start with GAME_DESIGN_DOCUMENT.md for core vision
2. **Programmers**: Jump to MECHANICS_DEEP_DIVE.md for technical specifications
3. **Artists/Audio**: Reference VISUAL_DESIGN_IMPLEMENTATION.md for style guide
4. **Quick Reference**: Use QUICK_REFERENCE.md for rapid lookups during development

---

## 🤝 Contributing

This is a comprehensive design document. If implementing this game:

1. Follow the core constraint: Source in light, Shade in darkness
2. Maintain minimalist aesthetic (clarity over decoration)
3. Test each mechanic thoroughly before combining
4. Prioritize player understanding over complexity

---

## 📜 License

This game design documentation is provided as creative inspiration. If you build this game, please:
- Credit the original concept appropriately
- Share your implementation with the community
- Maintain the core philosophical principles of elegant constraint-based design

---

## 🎉 Final Note

**Shade & Source** is about the beauty of duality and the power of simple rules creating complex challenges. Every design decision should serve clarity and player understanding.

**Where you stand determines where you cannot.**

Now go create something beautiful. 🌓

---

**Document Created**: November 10, 2025  
**Design Lead**: AI-Assisted Creative Design  
**Status**: Complete Design Package - Ready for Implementation
