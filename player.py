from circleshape import *
from constants import *

class Player(CircleShape):
    
    containers = ()
    
    # constructor
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) 
        self.rotation = 0
        self.timer = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS) 
        shot.velocity = pygame.Vector2(0, 1)   
        shot.velocity.rotate_ip(self.rotation)
        shot.velocity = shot.velocity * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        #rotate left/rigt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
            
        #move forward/backward
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        #shoot
        if keys[pygame.K_SPACE] and (self.timer <= 0):
            self.shoot()
        else:
            self.timer -= dt
        
        
        
class Shot(CircleShape):
        
    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt   