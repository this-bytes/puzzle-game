# 🎨 SHADE & SOURCE - Visual Design & Implementation Guide

## 🖼️ VISUAL IDENTITY

### Core Aesthetic Principles

#### 1. Minimalism as Clarity
- **Purpose**: Every visual element serves gameplay communication
- **No decoration**: If it doesn't inform player decisions, it doesn't exist
- **Geometric Purity**: All shapes are clean, mathematical, precise
- **Negative Space**: Emptiness is as important as form

#### 2. High-Contrast Communication
- **Binary States**: Light/Dark must be instantly recognizable
- **No Ambiguity**: Player should never question "Is this safe?"
- **Sharp Boundaries**: Shadows have crisp edges (no gradient confusion)
- **Consistent Rules**: Same visual = same meaning across all levels

#### 3. Minimal Color Palette

**Primary Palette**:
```
Background:    #1A1A1A (Near-black, slight warmth)
Light Zones:   #F5F5F5 (Off-white, slight cool)
Shadow Zones:  #0D0D0D (Pure black)
Neutral:       #808080 (Mid-grey for non-interactive elements)
```

**Accent Palette** (Sparing Use):
```
Source:        #FFE5CC (Warm peachy glow - subtle)
Shade:         #CCE5FF (Cool blue glow - subtle)
Inversion:     #E5CCFF (Purple/violet for inverted zones)
Hazard:        #FFCCCC (Slight red tint for danger)
Success:       #CCFFE5 (Slight green for goals/completion)
```

**Color Usage Rules**:
- Base gameplay: ONLY grayscale
- Accents: Maximum 10% opacity overlays
- No solid colors except in UI elements
- Color = information, not decoration

---

## 🎭 CHARACTER DESIGN

### The Source (Player Character)

**Visual Description**:
```
    ●  ← Simple circle head (8 units diameter)
   ╱│╲ ← Geometric body (12 units tall)
    │
   ╱ ╲ ← Minimal legs (animation: 2-frame walk cycle)
```

**Design Specifications**:
- **Shape**: Abstract geometric humanoid
- **Color**: Pure white with #FFE5CC glow (5% opacity)
- **Size**: 20 units tall × 10 units wide
- **Animation States**:
  - Idle: Subtle breathing motion (2-second cycle)
  - Walk: 2-frame cycle (seamless loop)
  - Jump: Arc with slight squash/stretch
  - Death: Instant fade to particles (0.5 seconds)
  
**Visual Feedback**:
- **Safe in Light**: Normal appearance, slight warm glow
- **Approaching Shadow**: Border pulse (red tint, 2Hz)
- **In Shadow**: Instant desaturation → fade

### The Shade (Shadow Character)

**Visual Description**:
```
    ●  ← Same silhouette as Source
   ╱│╲ ← But rendered as pure black shadow
    │
   ╱ ╲ ← No internal detail, flat black
```

**Design Specifications**:
- **Shape**: Exact silhouette match to Source
- **Color**: Pure black (#000000) with #CCE5FF glow (3% opacity)
- **Size**: Identical to Source (maintains perspective illusion)
- **Animation**: Mirrors Source animation (locked movement)
- **Projection**: Always connected to Source by visible line (subtle, #404040)

**Visual Feedback**:
- **Safe in Darkness**: Normal shadow appearance, slight cool glow
- **Approaching Light**: Border pulse (red tint, 2Hz)
- **In Light**: Instant desaturation → fade

**The Link** (Visual Connection):
- Subtle line from Source to Shade (#404040, 1-pixel width)
- Shows shadow projection direction
- Helps player understand spatial relationship
- Fades when Shade is far from Source

---

## 💡 LIGHT SOURCE VISUAL DESIGN

### Static Light (Omnidirectional)

```
     ╱ │ ╲      ← Light rays (subtle, animated)
    ╱  │  ╲
   ╱   │   ╲
  ╱    ●    ╲   ← Light source (circular, white glow)
       │
     [Cone]     ← Visible light volume (20% opacity)
```

**Specifications**:
- **Source**: 6-unit diameter circle, white (#F5F5F5)
- **Glow**: Radial gradient (inner: 100% opacity, outer: 0%)
- **Rays**: 8 rays, rotating slowly (20-second rotation)
- **Volume**: Light cone visible as subtle overlay
- **Animation**: Subtle pulse (1-second cycle, ±5% brightness)

### Moveable Lamp

```
   [Handle]     ← Visual grab point
      │
    ┌───┐       ← Lamp housing (geometric)
    │ ● │       ← Light source
    └───┘
      │
   [Beam]       ← Directional light cone
```

**Specifications**:
- **Size**: 12 units tall × 8 units wide
- **Handle**: Visual indicator for "pushable" (distinct color/pattern)
- **Direction**: Shows light beam direction clearly
- **Interaction**: Subtle glow when Source is near (indicates interactive)

### Patrol Light (Automated)

```
════●════════●════ ← Rail track (visible, grey)
    ↓        ↓
  [Light] [Position indicator dots]
```

**Specifications**:
- **Rail**: Visible track (2-pixel line, #606060)
- **Light**: Same as static light but with motion blur trail
- **Position Dots**: Show waypoints on rail
- **Speed Indicator**: Subtle trail effect (faster = longer trail)
- **Prediction**: Ghost image shows next position (optional accessibility feature)

### Prism

```
    [Input]
      │
      ▼
   ╱─◊─╲   ← Crystal shape (geometric diamond)
  ╱  │  ╲
 Beam Beam Beam
```

**Specifications**:
- **Shape**: Geometric crystal (diamond/hexagon)
- **Material**: Translucent with refraction effect (subtle)
- **Color**: Slight prismatic edge (rainbow shimmer, very subtle)
- **Beams**: Output beams clearly visible, color-coded if multiple
- **Rotation Handle**: Circular arrow indicator when rotatable

---

## 🌍 ENVIRONMENT DESIGN

### Platform Design

**Standard Platform**:
```
═══════════════
```
- 2-unit thick horizontal surfaces
- Pure geometric shapes (rectangles, squares)
- Color: #808080 (neutral grey)
- Shadow-casting enabled

**Climbable Wall**:
```
║
║ ← Subtle texture (grid pattern)
║
```
- Vertical surfaces with grip indicator
- Distinct visual pattern (dotted/gridded)
- Shows Shade can traverse when in shadow

**Hazard Platform**:
```
▓▓▓▓▓▓▓▓▓▓▓▓▓ ← Different pattern/texture
```
- Kills both Source AND Shade on contact
- Distinct pattern (diagonal lines, checkerboard)
- Slight red tint (#FFCCCC at 5% opacity)

### Background Layers

**Layer 1: Far Background**
- Deep void (#0D0D0D)
- Subtle particle field (stars/dust, barely visible)
- No parallax (maintains geometric simplicity)

**Layer 2: Mid Background**
- Architectural silhouettes (geometric shapes)
- Creates depth without distraction
- 30% opacity, pure black

**Layer 3: Gameplay Plane**
- All interactive elements
- Full opacity, clear contrast
- This is where eyes should focus

**Layer 4: Foreground (Rare)**
- Occasional framing elements
- Very subtle, creates depth
- Never obscures gameplay elements

---

## 🎬 ANIMATION PRINCIPLES

### Movement Animation

**Source Walk Cycle**:
```
Frame 1:  ╱│╲    Frame 2:  ╱│╲
           │               │
          ╱ ╲             ╱ ╲
```
- 2 frames only (minimalist)
- 0.2 seconds per frame
- Subtle bounce (2-pixel vertical shift)

**Shadow Projection Update**:
- Real-time calculation (60 FPS)
- Smooth interpolation between positions
- No frame-based animation (continuous)

### Interaction Animation

**Light Source Move**:
- Source pushes lamp: Lamp moves smoothly (ease-in-out)
- Shadow updates in real-time during push
- Subtle particle effect at contact point

**Prism Rotation**:
- Rotate in 15° increments (smooth interpolation)
- All output beams rotate simultaneously
- 0.3-second transition time
- Ease-in-out easing function

**Switch/Button Activation**:
- Press: 0.1-second depression animation
- Trigger: Immediate effect on connected objects
- Visual feedback: Color flash (success green)

### Death Animation

**Source Death**:
```
Frame 1:  ╱│╲     Frame 2:  ⚬ ⚬     Frame 3:  · ·
           │                ⚬ ⚬                · ·
          ╱ ╲              ⚬ ⚬

(Desaturate) → (Particle burst) → (Fade out)
```
- 0.5 seconds total
- Instant desaturation (0.05s)
- Particle dispersion (0.3s)
- Fade to nothing (0.15s)

**Shade Death**:
- Same animation as Source
- Blue-tinted particles instead of warm
- Occurs simultaneously if both die

**Reset Transition**:
- 1-second smooth rewind effect
- Ghostly trail shows return to start position
- Audio: Soft reverse whoosh

---

## 🎮 UI/UX DESIGN

### HUD (Heads-Up Display)

**Minimal HUD Philosophy**: Show only essential information

**On-Screen Elements**:
```
┌──────────────────────────────────────┐
│ Level 3: Interacting Shadows    [?] │ ← Top: Level name + hint button
│                                      │
│                                      │
│         [GAMEPLAY AREA]              │
│                                      │
│                                      │
│                                      │
│ Deaths: 5        Time: 1:32      [R]│ ← Bottom: Stats + reset button
└──────────────────────────────────────┘
```

**Font**: 
- Geometric sans-serif (e.g., Futura, Avenir, or custom)
- Size: 14pt for labels, 12pt for values
- Color: #C0C0C0 (light grey, doesn't distract)
- Position: Top corners and bottom bar

**Button Indicators**:
- Keyboard: Show key in square bracket `[R]`
- Gamepad: Show button icon
- Touch: Show gesture icon

### Menu System

**Main Menu**:
```
╔════════════════════════════════════╗
║                                    ║
║         SHADE & SOURCE             ║
║                                    ║
║            ●   ●                   ║ ← Animated Source/Shade
║           ╱│╲ ╱│╲                  ║
║            │   │                   ║
║           ╱╲  ╱╲                   ║
║                                    ║
║         > Start Game               ║
║           Level Select             ║
║           Options                  ║
║           Credits                  ║
║                                    ║
╚════════════════════════════════════╝
```

**Design Principles**:
- Same minimalist aesthetic as gameplay
- Animated Source/Shade in background (subtle movement)
- Selection: White text with gentle glow
- Unselected: Grey text (#808080)
- Navigation: Smooth fades (0.2s transitions)

**Level Select Screen**:
```
╔════════════════════════════════════╗
║  Level 1   Level 2   Level 3       ║
║  ✓ Gold    ✓ Silver  ○ Locked      ║
║                                    ║
║  [Preview of Level 2]              ║
║                                    ║
║  Best Time: 0:45                   ║
║  Deaths: 3                         ║
║  Moves: 12                         ║
║                                    ║
║       [Play] [Reset Stats]         ║
╚════════════════════════════════════╝
```

**Completion Indicators**:
- ✓ Gold: Completed under par time + minimal deaths
- ✓ Silver: Completed, but not optimal
- ✓ Bronze: Completed with many attempts
- ○ Locked: Not yet accessible

### Pause Menu (In-Game)

```
┌──────────────────┐
│   P A U S E D    │
│                  │
│  > Continue      │
│    Restart       │
│    Options       │
│    Quit to Menu  │
│                  │
└──────────────────┘
```

**Overlay**:
- Darken gameplay (50% opacity black overlay)
- Blur background slightly (subtle depth)
- Menu centered, clean borders
- Same minimalist style

---

## 🔊 AUDIO DESIGN SPECIFICATIONS

### Ambient Soundscape

**Base Layer** (Continuous):
- Low frequency drone (60 Hz)
- Subtle harmonic overtones
- No melody or rhythm
- Volume: -30 dB

**Dynamic Layer** (Responds to gameplay):
- Safe position: Consonant harmonics (major chords)
- Danger proximity: Dissonant intervals (tritones)
- Multiple constraints: Harmonic density increases
- Resolution: Returns to base drone

### Sound Effects Library

**Movement**:
- Source footstep: Soft tap (wood block sound, -20 dB)
- Source jump: Gentle whoosh up + land thump
- Shade movement: No sound (silent shadow)

**Light Interaction**:
- Push lamp: Smooth friction sound (continuous)
- Rotate prism: Crystal chime (pitch based on rotation speed)
- Activate switch: Mechanical click (satisfying, -15 dB)
- Patrol light pass: Subtle whoosh (doppler effect)

**Feedback**:
- Danger proximity: High-frequency shimmer (2000 Hz, subtle)
- Death: Harmonic collapse (all frequencies drop to silence)
- Level complete: Ascending arpeggio (major chord resolution)
- Reset: Reverse whoosh with pitch down

**UI**:
- Menu navigate: Soft blip (sine wave, 800 Hz)
- Menu select: Gentle confirmation (1000 Hz, short decay)
- Pause: Time-stop effect (pitch bend down)
- Unpause: Time-start effect (pitch bend up)

### Audio Mixing Guidelines

**Priority Layers**:
1. Gameplay feedback (deaths, danger warnings) - Highest priority
2. Environmental audio (light movements) - Medium priority
3. Ambient soundscape - Lowest priority (always present but subtle)

**Accessibility**:
- Visual substitutes for all critical audio cues
- Volume sliders for each layer independently
- Mono audio option (no stereo requirement)
- Subtitle system for any narrative/tutorial text

---

## 🛠️ TECHNICAL IMPLEMENTATION ROADMAP

### Phase 1: Core Prototype (Weeks 1-4)

**Week 1: Foundation**
- [ ] Setup game engine (Unity/Godot/custom)
- [ ] Basic 2D rendering pipeline
- [ ] Input handling (keyboard, gamepad)
- [ ] Scene management system

**Week 2: Core Mechanics**
- [ ] Source character controller (movement, collision)
- [ ] Single light source implementation
- [ ] Shadow projection mathematics (2D raycasting)
- [ ] Shade entity (follows Source shadow)
- [ ] Death detection (Source in shadow, Shade in light)

**Week 3: Level 1 Implementation**
- [ ] Platform/obstacle system
- [ ] Laser gate mechanic
- [ ] Win condition detection
- [ ] Reset/restart functionality
- [ ] Basic visual assets (placeholder art)

**Week 4: Polish & Test**
- [ ] Death animation
- [ ] Level transition
- [ ] Basic UI (level name, restart button)
- [ ] Playtest with 5-10 users
- [ ] Iterate based on feedback

### Phase 2: Advanced Mechanics (Weeks 5-8)

**Week 5: Multi-Plane Projection**
- [ ] Wall shadow projection
- [ ] Rotatable light source
- [ ] Level 2 implementation
- [ ] Camera system improvements

**Week 6: Multiple Light Sources**
- [ ] Multi-shadow system
- [ ] Light source interaction (overlapping)
- [ ] Environmental shadow objects
- [ ] Level 3 implementation

**Week 7: New Mechanics - Patrol Light**
- [ ] Automated movement system
- [ ] Path/rail editor tool
- [ ] Timing-based puzzle implementation
- [ ] Levels 4-5 implementation

**Week 8: New Mechanics - Prism**
- [ ] Beam splitting mathematics
- [ ] Rotation system for prisms
- [ ] Multi-shadow constraint validation
- [ ] Levels 6-7 implementation

### Phase 3: Advanced Systems (Weeks 9-12)

**Week 9: Inversion Field**
- [ ] Zone-based rule inversion
- [ ] Visual field effects
- [ ] Cognitive challenge levels
- [ ] Levels 8-9 implementation

**Week 10: Polish & Visual Design**
- [ ] Final art asset creation (minimalist style)
- [ ] Particle system (deaths, interactions)
- [ ] Lighting effects (glows, shadows)
- [ ] Animation polish (easing, timing)

**Week 11: Audio Implementation**
- [ ] Ambient soundscape system
- [ ] Sound effects integration
- [ ] Dynamic audio (responds to game state)
- [ ] Audio mixing and balancing

**Week 12: UI/UX Completion**
- [ ] Main menu system
- [ ] Level select with stats
- [ ] Options menu (accessibility features)
- [ ] Pause menu
- [ ] Tutorial/hint system

### Phase 4: Content & Testing (Weeks 13-16)

**Week 13: Full Level Suite**
- [ ] Levels 10-12 (final challenges)
- [ ] Difficulty curve balancing
- [ ] Par time/move calculations
- [ ] Achievement system

**Week 14: Comprehensive Testing**
- [ ] Full playthrough testing
- [ ] Edge case bug fixing
- [ ] Performance optimization
- [ ] Accessibility testing

**Week 15: Feedback & Iteration**
- [ ] External playtesting (20+ users)
- [ ] Difficulty adjustment based on data
- [ ] Tutorial refinement
- [ ] Quality of life improvements

**Week 16: Launch Preparation**
- [ ] Marketing materials (trailer, screenshots)
- [ ] Store page setup (Steam, itch.io, etc.)
- [ ] Press kit creation
- [ ] Final bug fixes and polish

### Phase 5: Post-Launch (Ongoing)

**Weeks 17+**
- [ ] Monitor player feedback and analytics
- [ ] Patch critical bugs immediately
- [ ] Plan DLC/expansion content
- [ ] Community engagement (forums, social media)
- [ ] Consider speedrun community tools
- [ ] Mobile port exploration (if applicable)

---

## 🎯 TECHNOLOGY STACK RECOMMENDATIONS

### Game Engine Options

**Option 1: Unity (Recommended for 2D)**
- **Pros**: Excellent 2D tools, large asset store, cross-platform export
- **Cons**: Overkill for minimalist game, license considerations
- **Best For**: Teams familiar with Unity, planning mobile ports

**Option 2: Godot (Recommended for Indie)**
- **Pros**: Free/open-source, lightweight, great 2D engine, GDScript is accessible
- **Cons**: Smaller community than Unity, fewer third-party assets
- **Best For**: Solo developers, open-source enthusiasts, small teams

**Option 3: Custom Engine (HTML5/JavaScript)**
- **Pros**: Maximum control, web-native, easy distribution
- **Cons**: More development time, need to build everything
- **Best For**: Web game developers, portfolio projects, browser-first strategy

**Option 4: GameMaker Studio 2**
- **Pros**: Excellent for 2D, drag-and-drop + code, rapid prototyping
- **Cons**: License cost, less transferable skills
- **Best For**: 2D-focused developers, rapid iteration needs

### Recommended Tools

**Art/Animation**:
- **Vector Graphics**: Adobe Illustrator / Inkscape (free)
- **Sprite Creation**: Aseprite (pixel art) / Figma (vector)
- **Animation**: Spine (complex) / built-in engine tools (simple)

**Audio**:
- **Sound Design**: Audacity (free) / FL Studio (professional)
- **Music**: LMMS (free) / Ableton Live (professional)
- **Procedural Audio**: Pure Data / Bfxr (free)

**Level Design**:
- **Level Editor**: In-engine tool (build custom editor)
- **Planning**: Graph paper / Miro / Excalidraw
- **Testing**: Integrated playtest mode in editor

**Version Control**:
- **Git**: GitHub / GitLab
- **Large Files**: Git LFS for assets
- **Collaboration**: GitHub Projects for task management

---

## 📊 SUCCESS METRICS & ANALYTICS

### Key Performance Indicators (KPIs)

**Player Engagement**:
- Average session length (target: 20-30 minutes)
- Level completion rate (target: >70% for first 3 levels)
- Return rate (% of players returning within 7 days)

**Difficulty Metrics**:
- Deaths per level (target: 5-10 for tutorial, 10-20 for advanced)
- Time to complete per level
- Hint usage frequency
- Skip level usage (indicates too difficult)

**Quality Metrics**:
- Crash rate (target: <0.1%)
- Frame rate consistency (target: 60 FPS on target hardware)
- Load times (target: <2 seconds per level)

**Business Metrics** (if applicable):
- Sales conversion rate
- Review scores (target: >4.0/5.0 average)
- Refund rate (target: <5%)
- Wishlist conversion (target: >30%)

### Analytics Integration

**Recommended Platform**: Unity Analytics / GameAnalytics (free tier)

**Track These Events**:
- Level started
- Level completed (with time and deaths)
- Player death (with cause: "Source hit shadow" vs "Shade hit light")
- Hint requested
- Level reset
- Prism rotated, lamp moved (interaction tracking)
- Menu navigation
- Settings changed (accessibility features used)

**Privacy Considerations**:
- Opt-in analytics (GDPR compliant)
- No personal data collection
- Anonymous session IDs only
- Clear privacy policy

---

## 🌟 MARKETING & COMMUNITY

### Target Audience

**Primary Audience**:
- Puzzle game enthusiasts (Portal, Braid, Limbo fans)
- Age: 18-35
- Platform: PC (Steam), potentially mobile
- Values: Clever mechanics over graphics, intellectual challenge

**Secondary Audience**:
- Indie game supporters
- Minimalist art/design fans
- Speedrunning community
- Educational institutions (geometry/logic teaching tool)

### Marketing Channels

**Pre-Launch**:
1. **Social Media**: Twitter/X, Reddit (r/indiegames, r/puzzles)
2. **Dev Blog**: Devlog series on development process
3. **GIFs/Short Videos**: Show clever puzzle solutions (shareable)
4. **Demo**: Free demo of first 3 levels (build wishlist)
5. **Influencer Outreach**: Puzzle game YouTubers/streamers

**Launch**:
1. **Press Kit**: Send to indie game journalists
2. **Launch Trailer**: 60-90 seconds, show core mechanic elegantly
3. **Steam/Itch Launch**: Coordinate for maximum visibility
4. **Community Events**: Speedrun competition, level design contest

**Post-Launch**:
1. **Content Updates**: New levels, mechanics (free DLC)
2. **Community Highlight**: Feature player speedruns, creative solutions
3. **Educational Partnerships**: Reach out to schools/educators
4. **Port Announcements**: Mobile, console (if applicable)

### Community Building

**Discord Server** (Optional):
- General discussion channel
- Speedrun channel (leaderboards, strategies)
- Bug reports channel
- Fan art/creations channel

**Speedrun.com Leaderboard**:
- Set up official leaderboards
- Define categories (Any%, 100%, No Deaths)
- Engage with speedrun community

**Level Editor** (Future Feature):
- Allow players to create custom levels
- Share via code or integrated workshop
- Featured levels curated by developer

---

## 🏁 FINAL CHECKLIST (Before Launch)

### Technical
- [ ] All levels completable (tested by external players)
- [ ] No game-breaking bugs
- [ ] Consistent 60 FPS on target hardware
- [ ] All platforms tested (Windows, Mac, Linux if applicable)
- [ ] Save system works reliably
- [ ] Settings persist correctly

### Content
- [ ] 12+ levels complete with varied challenges
- [ ] Tutorial effectively teaches mechanics
- [ ] Difficulty curve feels fair
- [ ] All achievements achievable
- [ ] Credits complete and accurate

### Polish
- [ ] All art assets final (no placeholders)
- [ ] All audio mixed and balanced
- [ ] UI is clear and responsive
- [ ] Animations smooth (no jank)
- [ ] Transitions feel good (loading, level change, death)

### Accessibility
- [ ] Colorblind modes (if using color beyond greyscale)
- [ ] Scalable UI/text
- [ ] Remappable controls
- [ ] Visual audio cues
- [ ] Adjustable difficulty options

### Business
- [ ] Store page complete (description, tags, screenshots)
- [ ] Trailer uploaded and polished
- [ ] Press kit available
- [ ] Social media accounts active
- [ ] Community channels ready (Discord, etc.)
- [ ] Launch date set and announced

### Legal
- [ ] Privacy policy (if collecting analytics)
- [ ] Terms of service
- [ ] Asset licenses verified (all art/audio original or licensed)
- [ ] ESRB/PEGI rating obtained (if required)

---

*End of Visual Design & Implementation Guide*

**Document Version**: 1.0  
**Created**: November 10, 2025  
**Companion to**: GAME_DESIGN_DOCUMENT.md, MECHANICS_DEEP_DIVE.md  
**Status**: Complete Implementation Roadmap

---

## 🎉 FINAL WORDS

**Shade & Source** is a game about duality, constraint, and elegant problem-solving. The beauty lies in its simplicity—two entities, one control scheme, and the interplay of light and shadow. 

Every design decision should ask: *"Does this serve clarity or create ambiguity?"*

The answer should always be **clarity**. 

In a world of visual noise and mechanical complexity, **Shade & Source** stands as a testament to the power of restraint, the elegance of geometric truth, and the profound depth that emerges from simple rules rigorously applied.

**Where you stand determines where you cannot.**

Now go build it. 🌓
