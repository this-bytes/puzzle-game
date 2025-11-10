// Shade & Source - Level 1: The Basic Divide
// Implementation following LEVEL_1_IMPLEMENTATION.md specifications

// Constants
const UNIT_SIZE = 32; // pixels per grid unit
const GRID_WIDTH = 30;
const GRID_HEIGHT = 20;
const CANVAS_WIDTH = GRID_WIDTH * UNIT_SIZE;
const CANVAS_HEIGHT = GRID_HEIGHT * UNIT_SIZE;
const CAMERA_OFFSET_Y = 3 * UNIT_SIZE; // Offset to show shadow floor
const GRAVITY = 0.5;
const PAR_TIME = 15; // seconds

// Color palette from VISUAL_DESIGN_IMPLEMENTATION.md
const COLORS = {
    BACKGROUND: '#1A1A1A',
    LIGHT_ZONE: '#F5F5F5',
    SHADOW_ZONE: '#0D0D0D',
    NEUTRAL: '#808080',
    SOURCE_GLOW: '#FFE5CC',
    SHADE_GLOW: '#CCE5FF',
    GOAL: '#CCFFE5',
    LASER: '#FF6666',
    BRIDGE: '#A0A0A0',
    CONNECTION_LINE: '#404040'
};

// Game state
const game = {
    canvas: null,
    ctx: null,
    running: false,
    paused: false,
    won: false,
    startTime: 0,
    elapsedTime: 0,
    deaths: 0,
    keys: {},
    
    // Entities
    source: null,
    shade: null,
    light: null,
    platforms: [],
    laserGate: null,
    bridge: null,
    goal: null,
    
    // Animation
    lastFrameTime: 0,
    animationTime: 0
};

// Expose game for debugging
if (typeof window !== 'undefined') {
    window.game = game;
}

// Source character (player-controlled)
class Source {
    constructor(x, y) {
        this.startX = x;
        this.startY = y;
        this.x = x;
        this.y = y;
        this.width = 10;
        this.height = 20;
        this.vx = 0;
        this.vy = 0;
        this.speed = 4; // units per second
        this.jumpForce = 10;
        this.onGround = false;
        this.dead = false;
        this.deathTimer = 0;
    }
    
    update(dt) {
        if (this.dead) {
            this.deathTimer += dt;
            if (this.deathTimer >= 1.0) {
                this.reset();
                game.deaths++;
                updateUI();
            }
            return;
        }
        
        // Horizontal movement
        if (game.keys['ArrowLeft'] || game.keys['a'] || game.keys['A']) {
            this.vx = -this.speed;
        } else if (game.keys['ArrowRight'] || game.keys['d'] || game.keys['D']) {
            this.vx = this.speed;
        } else {
            this.vx = 0;
        }
        
        // Jump
        if ((game.keys[' '] || game.keys['w'] || game.keys['W']) && this.onGround) {
            this.vy = -this.jumpForce;
            this.onGround = false;
        }
        
        // Apply gravity
        this.vy += GRAVITY;
        
        // Update position
        this.x += this.vx * dt;
        this.y += this.vy * dt;
        
        // Collision with platforms
        this.onGround = false;
        for (let platform of game.platforms) {
            if (platform.layer !== 'shadowWorld' && this.checkCollision(platform)) {
                // Top collision (landing)
                if (this.vy > 0 && this.y + this.height <= platform.y + this.vy * dt + 5) {
                    this.y = platform.y - this.height;
                    this.vy = 0;
                    this.onGround = true;
                }
                // Bottom collision
                else if (this.vy < 0 && this.y >= platform.y + platform.height) {
                    this.y = platform.y + platform.height;
                    this.vy = 0;
                }
                // Side collisions
                if (this.vx > 0 && this.x + this.width > platform.x && 
                    this.x < platform.x) {
                    this.x = platform.x - this.width;
                }
                else if (this.vx < 0 && this.x < platform.x + platform.width && 
                         this.x > platform.x) {
                    this.x = platform.x + platform.width;
                }
            }
        }
        
        // Bridge collision (if spawned and collidable)
        if (game.bridge && game.bridge.collidable && this.checkCollision(game.bridge)) {
            if (this.vy > 0 && this.y + this.height <= game.bridge.y + this.vy * dt + 5) {
                this.y = game.bridge.y - this.height;
                this.vy = 0;
                this.onGround = true;
            }
        }
        
        // Check death conditions
        this.checkDeath();
    }
    
    checkCollision(rect) {
        return this.x < rect.x + rect.width &&
               this.x + this.width > rect.x &&
               this.y < rect.y + rect.height &&
               this.y + this.height > rect.y;
    }
    
    checkDeath() {
        // Check if in light (safe for Source)
        const inLight = isInLight(this.x + this.width / 2, this.y + this.height / 2, game.light);
        
        if (!inLight) {
            this.die('shadow');
        }
        
        // Check out of bounds
        if (this.y > GRID_HEIGHT * UNIT_SIZE || this.y < -5 * UNIT_SIZE) {
            this.die('void');
        }
    }
    
    die(reason) {
        if (!this.dead) {
            this.dead = true;
            this.deathTimer = 0;
            console.log('Source died:', reason);
        }
    }
    
    reset() {
        this.x = this.startX;
        this.y = this.startY;
        this.vx = 0;
        this.vy = 0;
        this.dead = false;
        this.deathTimer = 0;
        this.onGround = false;
        
        // Reset bridge
        if (game.bridge) {
            game.bridge.visible = false;
            game.bridge.collidable = false;
            game.bridge.animationProgress = 0;
        }
    }
    
    draw(ctx) {
        if (this.dead && this.deathTimer > 0.5) {
            return; // Fade out
        }
        
        const screenX = this.x;
        const screenY = toScreenY(this.y, this.height);
        
        // Draw glow
        ctx.save();
        ctx.globalAlpha = 0.05;
        ctx.fillStyle = COLORS.SOURCE_GLOW;
        ctx.beginPath();
        ctx.arc(screenX + this.width / 2, screenY + this.height / 2, 15, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
        
        // Draw character (geometric humanoid)
        ctx.fillStyle = '#FFFFFF';
        
        // Head (circle)
        ctx.beginPath();
        ctx.arc(screenX + this.width / 2, screenY + 5, 4, 0, Math.PI * 2);
        ctx.fill();
        
        // Body
        ctx.fillRect(screenX + this.width / 2 - 1, screenY + 9, 2, 8);
        
        // Arms
        ctx.beginPath();
        ctx.moveTo(screenX + this.width / 2, screenY + 11);
        ctx.lineTo(screenX + 2, screenY + 14);
        ctx.moveTo(screenX + this.width / 2, screenY + 11);
        ctx.lineTo(screenX + this.width - 2, screenY + 14);
        ctx.strokeStyle = '#FFFFFF';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // Legs
        ctx.beginPath();
        ctx.moveTo(screenX + this.width / 2, screenY + 17);
        ctx.lineTo(screenX + 3, screenY + 20);
        ctx.moveTo(screenX + this.width / 2, screenY + 17);
        ctx.lineTo(screenX + this.width - 3, screenY + 20);
        ctx.stroke();
    }
}

// Shade character (shadow projection)
class Shade {
    constructor() {
        this.x = 0;
        this.y = 0;
        this.width = 10;
        this.height = 20;
        this.dead = false;
    }
    
    update() {
        // Calculate shadow projection
        const shadowPlaneY = -2; // Grid units
        const projectedPos = calculateShadePosition(
            game.source.x + game.source.width / 2,
            game.source.y + game.source.height / 2,
            game.light.x,
            game.light.y,
            shadowPlaneY
        );
        
        this.x = projectedPos.x - this.width / 2;
        this.y = projectedPos.y - this.height / 2;
        
        // Check death conditions
        this.checkDeath();
        
        // Check laser gate collision
        if (game.laserGate && game.laserGate.active) {
            if (this.checkCollisionWithLaser()) {
                game.laserGate.blocked = true;
                if (!game.bridge.visible) {
                    game.bridge.spawn();
                }
            } else {
                game.laserGate.blocked = false;
            }
        }
    }
    
    checkCollisionWithLaser() {
        const laser = game.laserGate;
        return this.x < laser.x + laser.width &&
               this.x + this.width > laser.x &&
               this.y < laser.y + laser.beamHeight &&
               this.y + this.height > laser.y;
    }
    
    checkDeath() {
        // Shade dies in light
        const inLight = isInLight(this.x + this.width / 2, this.y + this.height / 2, game.light);
        
        if (inLight && !game.source.dead) {
            game.source.die('shade in light');
        }
    }
    
    draw(ctx) {
        if (game.source.dead) return;
        
        const screenX = this.x;
        const screenY = toScreenY(this.y, this.height);
        
        // Debug: Draw a marker even if off-screen
        ctx.save();
        ctx.fillStyle = '#FF00FF'; // Magenta for debugging
        ctx.fillRect(Math.max(0, screenX), Math.max(0, screenY), 5, 5);
        ctx.restore();
        
        // Draw connection line to Source
        ctx.save();
        ctx.strokeStyle = COLORS.CONNECTION_LINE;
        ctx.lineWidth = 1;
        ctx.globalAlpha = 0.3;
        ctx.beginPath();
        const sourceScreenX = game.source.x + game.source.width / 2;
        const sourceScreenY = toScreenY(game.source.y, game.source.height / 2);
        ctx.moveTo(sourceScreenX, sourceScreenY);
        ctx.lineTo(Math.max(0, screenX + this.width / 2), Math.max(0, screenY + this.height / 2));
        ctx.stroke();
        ctx.restore();
        
        // Only draw shade if on screen
        if (screenX < -this.width || screenX > CANVAS_WIDTH || screenY < -this.height || screenY > CANVAS_HEIGHT) {
            return; // Off screen
        }
        
        // Draw glow
        ctx.save();
        ctx.globalAlpha = 0.03;
        ctx.fillStyle = COLORS.SHADE_GLOW;
        ctx.beginPath();
        ctx.arc(screenX + this.width / 2, screenY + this.height / 2, 15, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
        
        // Draw character (same silhouette as Source)
        ctx.fillStyle = '#000000';
        
        // Head
        ctx.beginPath();
        ctx.arc(screenX + this.width / 2, screenY + 5, 4, 0, Math.PI * 2);
        ctx.fill();
        
        // Body
        ctx.fillRect(screenX + this.width / 2 - 1, screenY + 9, 2, 8);
        
        // Arms
        ctx.beginPath();
        ctx.moveTo(screenX + this.width / 2, screenY + 11);
        ctx.lineTo(screenX + 2, screenY + 14);
        ctx.moveTo(screenX + this.width / 2, screenY + 11);
        ctx.lineTo(screenX + this.width - 2, screenY + 14);
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // Legs
        ctx.beginPath();
        ctx.moveTo(screenX + this.width / 2, screenY + 17);
        ctx.lineTo(screenX + 3, screenY + 20);
        ctx.moveTo(screenX + this.width / 2, screenY + 17);
        ctx.lineTo(screenX + this.width - 3, screenY + 20);
        ctx.stroke();
    }
}

// Light source
class Light {
    constructor(x, y, radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.pulseTime = 0;
    }
    
    update(dt) {
        this.pulseTime += dt;
    }
    
    draw(ctx) {
        const screenX = this.x;
        const screenY = CANVAS_HEIGHT - this.y;
        
        // Pulse animation
        const pulse = 1.0 + Math.sin(this.pulseTime * Math.PI * 2) * 0.05;
        
        // Draw light volume (semi-transparent circle)
        ctx.save();
        const gradient = ctx.createRadialGradient(screenX, screenY, 0, screenX, screenY, this.radius);
        gradient.addColorStop(0, 'rgba(245, 245, 245, 0.15)');
        gradient.addColorStop(0.7, 'rgba(245, 245, 245, 0.05)');
        gradient.addColorStop(1, 'rgba(245, 245, 245, 0)');
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(screenX, screenY, this.radius * pulse, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
        
        // Draw light source
        ctx.fillStyle = COLORS.LIGHT_ZONE;
        ctx.beginPath();
        ctx.arc(screenX, screenY, 6 * pulse, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw rays (rotating slowly)
        ctx.save();
        ctx.strokeStyle = 'rgba(245, 245, 245, 0.1)';
        ctx.lineWidth = 1;
        for (let i = 0; i < 8; i++) {
            const angle = (i / 8) * Math.PI * 2 + this.pulseTime * 0.5;
            ctx.beginPath();
            ctx.moveTo(screenX, screenY);
            ctx.lineTo(
                screenX + Math.cos(angle) * this.radius,
                screenY + Math.sin(angle) * this.radius
            );
            ctx.stroke();
        }
        ctx.restore();
    }
}

// Platform
class Platform {
    constructor(x, y, width, height, layer = 'normal') {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.layer = layer;
    }
    
    draw(ctx) {
        const screenX = this.x;
        const screenY = toScreenY(this.y, this.height);
        
        ctx.fillStyle = this.layer === 'shadowWorld' ? '#0D0D0D' : COLORS.NEUTRAL;
        ctx.fillRect(screenX, screenY, this.width, this.height);
        
        // Border
        ctx.strokeStyle = '#606060';
        ctx.lineWidth = 1;
        ctx.strokeRect(screenX, screenY, this.width, this.height);
    }
}

// Laser gate
class LaserGate {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.beamHeight = 200; // Extends upward
        this.active = true;
        this.blocked = false;
    }
    
    draw(ctx) {
        if (!this.active) return;
        
        const screenX = this.x;
        const screenY = toScreenY(this.y);
        
        // Draw laser beam
        ctx.save();
        ctx.fillStyle = this.blocked ? 'rgba(102, 255, 102, 0.3)' : 'rgba(255, 102, 102, 0.3)';
        ctx.fillRect(screenX, screenY - this.beamHeight, this.width, this.beamHeight);
        
        // Beam edges
        ctx.strokeStyle = this.blocked ? '#66FF66' : COLORS.LASER;
        ctx.lineWidth = 2;
        ctx.strokeRect(screenX, screenY - this.beamHeight, this.width, this.beamHeight);
        ctx.restore();
        
        // Draw gate base
        ctx.fillStyle = '#404040';
        ctx.fillRect(screenX - 2, screenY, this.width + 4, this.height);
    }
}

// Bridge
class Bridge {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.visible = false;
        this.collidable = false;
        this.animationProgress = 0;
        this.animationDuration = 0.5; // seconds
    }
    
    spawn() {
        this.visible = true;
        this.animationProgress = 0;
    }
    
    update(dt) {
        if (this.visible && this.animationProgress < 1.0) {
            this.animationProgress += dt / this.animationDuration;
            if (this.animationProgress >= 1.0) {
                this.animationProgress = 1.0;
                this.collidable = true;
            }
        }
    }
    
    draw(ctx) {
        if (!this.visible) return;
        
        const screenX = this.x;
        const screenY = toScreenY(this.y, this.height);
        
        // Ease-out animation
        const easeProgress = 1 - Math.pow(1 - this.animationProgress, 3);
        const currentWidth = this.width * easeProgress;
        
        ctx.fillStyle = COLORS.BRIDGE;
        ctx.fillRect(screenX, screenY, currentWidth, this.height);
        
        // Border
        ctx.strokeStyle = '#707070';
        ctx.lineWidth = 1;
        ctx.strokeRect(screenX, screenY, currentWidth, this.height);
    }
}

// Goal
class Goal {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.floatTime = 0;
    }
    
    update(dt) {
        this.floatTime += dt;
    }
    
    checkCollision(source) {
        return source.x < this.x + this.width &&
               source.x + source.width > this.x &&
               source.y < this.y + this.height &&
               source.y + source.height > this.y;
    }
    
    draw(ctx) {
        // Float animation
        const floatOffset = Math.sin(this.floatTime * Math.PI) * 0.5 * UNIT_SIZE;
        
        const screenX = this.x;
        const screenY = toScreenY(this.y, this.height) + floatOffset;
        
        // Draw glow
        ctx.save();
        ctx.globalAlpha = 0.2;
        ctx.fillStyle = '#00FF88';
        ctx.beginPath();
        ctx.arc(screenX + this.width / 2, screenY + this.height / 2, 20, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
        
        // Draw goal
        ctx.fillStyle = COLORS.GOAL;
        ctx.fillRect(screenX, screenY, this.width, this.height);
        
        // Border
        ctx.strokeStyle = '#00FF88';
        ctx.lineWidth = 2;
        ctx.strokeRect(screenX, screenY, this.width, this.height);
    }
}

// Helper functions
function toScreenY(gameY, height = 0) {
    return CANVAS_HEIGHT - (gameY + height) - CAMERA_OFFSET_Y;
}

function calculateShadePosition(sourceX, sourceY, lightX, lightY, shadowPlaneY) {
    // Shadow projection mathematics from MECHANICS_DEEP_DIVE.md
    // Note: positions are in pixel coordinates, not grid units
    const dx = sourceX - lightX;
    const dy = sourceY - lightY;
    
    // Shadow plane is at Y = -2 grid units = -64 pixels
    const shadowPlanePixels = shadowPlaneY * UNIT_SIZE;
    
    // Calculate where shadow ray intersects shadow plane
    // Avoid division by zero
    if (Math.abs(dy) < 0.1) {
        return { x: sourceX, y: shadowPlanePixels };
    }
    
    const t = (shadowPlanePixels - lightY) / dy;
    
    const shadeX = lightX + (dx * t);
    const shadeY = shadowPlanePixels;
    
    return { x: shadeX, y: shadeY };
}

function isInLight(x, y, light) {
    // All coordinates are in game coordinate system (pixels, Y-up from bottom)
    const distance = Math.sqrt(
        Math.pow(x - light.x, 2) + 
        Math.pow(y - light.y, 2)
    );
    
    return distance <= light.radius;
}

function updateUI() {
    document.getElementById('deaths').textContent = game.deaths;
    
    const minutes = Math.floor(game.elapsedTime / 60);
    const seconds = Math.floor(game.elapsedTime % 60);
    document.getElementById('timer').textContent = 
        `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

function showWinScreen() {
    game.won = true;
    const winScreen = document.getElementById('winScreen');
    const finalTime = document.getElementById('finalTime');
    const finalDeaths = document.getElementById('finalDeaths');
    const parTime = document.getElementById('parTime');
    
    const minutes = Math.floor(game.elapsedTime / 60);
    const seconds = Math.floor(game.elapsedTime % 60);
    finalTime.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
    finalDeaths.textContent = game.deaths;
    
    if (game.elapsedTime <= PAR_TIME) {
        parTime.textContent = `Par Time: ${PAR_TIME}s ⭐`;
        parTime.style.color = '#CCFFE5';
    } else {
        parTime.textContent = `Par Time: ${PAR_TIME}s`;
        parTime.style.color = '#808080';
    }
    
    winScreen.style.display = 'block';
}

// Initialize game
function init() {
    game.canvas = document.getElementById('gameCanvas');
    game.ctx = game.canvas.getContext('2d');
    
    // Create entities following LEVEL_1_IMPLEMENTATION.md coordinates
    game.source = new Source(6 * UNIT_SIZE, 5 * UNIT_SIZE);
    game.shade = new Shade();
    game.light = new Light(15 * UNIT_SIZE, 18 * UNIT_SIZE, 18 * UNIT_SIZE); // Increased radius to cover playable area
    
    // Platforms
    game.platforms = [
        new Platform(0, 3 * UNIT_SIZE, 30 * UNIT_SIZE, 2 * UNIT_SIZE), // Ground
        new Platform(0, 7 * UNIT_SIZE, 14 * UNIT_SIZE, 2 * UNIT_SIZE), // Mid left
        new Platform(20 * UNIT_SIZE, 7 * UNIT_SIZE, 10 * UNIT_SIZE, 2 * UNIT_SIZE), // Mid right
        new Platform(0, 11 * UNIT_SIZE, 30 * UNIT_SIZE, 2 * UNIT_SIZE), // Top
        new Platform(0, -2 * UNIT_SIZE, 30 * UNIT_SIZE, 2 * UNIT_SIZE, 'shadowWorld') // Shadow floor
    ];
    
    // Laser gate
    game.laserGate = new LaserGate(12 * UNIT_SIZE, -5 * UNIT_SIZE, 6 * UNIT_SIZE, 3 * UNIT_SIZE);
    
    // Bridge
    game.bridge = new Bridge(14 * UNIT_SIZE, 7 * UNIT_SIZE, 6 * UNIT_SIZE, 2 * UNIT_SIZE);
    
    // Goal
    game.goal = new Goal(18 * UNIT_SIZE, 12 * UNIT_SIZE, 3 * UNIT_SIZE, 3 * UNIT_SIZE);
    
    // Input handling
    window.addEventListener('keydown', (e) => {
        game.keys[e.key] = true;
        
        if (e.key === 'r' || e.key === 'R') {
            game.source.reset();
            game.deaths++;
            updateUI();
        }
        
        if (e.key === 'Escape') {
            game.paused = !game.paused;
        }
    });
    
    window.addEventListener('keyup', (e) => {
        game.keys[e.key] = false;
    });
    
    game.running = true;
    game.startTime = Date.now();
    requestAnimationFrame(gameLoop);
}

// Game loop
function gameLoop(timestamp) {
    if (!game.running) return;
    
    const dt = Math.min((timestamp - game.lastFrameTime) / 1000, 0.1) || 0.016;
    game.lastFrameTime = timestamp;
    
    if (!game.paused && !game.won) {
        game.elapsedTime = (Date.now() - game.startTime) / 1000;
        game.animationTime += dt;
        
        // Update
        game.source.update(dt);
        game.shade.update();
        game.light.update(dt);
        game.goal.update(dt);
        game.bridge.update(dt);
        
        // Check win condition
        if (!game.source.dead && game.goal.checkCollision(game.source)) {
            showWinScreen();
        }
        
        updateUI();
    }
    
    // Render
    render();
    
    requestAnimationFrame(gameLoop);
}

function render() {
    const ctx = game.ctx;
    
    // Clear canvas
    ctx.fillStyle = COLORS.BACKGROUND;
    ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    
    // Draw platforms
    for (let platform of game.platforms) {
        platform.draw(ctx);
    }
    
    // Draw laser gate
    game.laserGate.draw(ctx);
    
    // Draw bridge
    game.bridge.draw(ctx);
    
    // Draw goal
    game.goal.draw(ctx);
    
    // Draw light
    game.light.draw(ctx);
    
    // Draw shade
    game.shade.draw(ctx);
    
    // Draw source
    game.source.draw(ctx);
    
    // Draw paused overlay
    if (game.paused) {
        ctx.save();
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
        ctx.fillStyle = '#F5F5F5';
        ctx.font = '24px "Courier New"';
        ctx.textAlign = 'center';
        ctx.fillText('PAUSED', CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2);
        ctx.font = '14px "Courier New"';
        ctx.fillText('Press ESC to resume', CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + 30);
        ctx.restore();
    }
}

// Start game when page loads
window.addEventListener('load', init);
