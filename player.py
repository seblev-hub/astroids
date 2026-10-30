import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot


class Player(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0
        self.cooldown: float = 0


    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt) -> None:
        self.rotation +=  (PLAYER_TURN_SPEED * dt)

    def shoot(self) -> None:
        if not self.cooldown > 0:
            bullet = Shot(self.position.x, self.position.y)
            dir_vector = pygame.Vector2(0, 1)
            forward_dir = dir_vector.rotate(self.rotation)
            bullet.velocity =  forward_dir * PLAYER_SHOOT_SPEED
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS



    def move(self, dt) -> None:
        dir_vector = pygame.Vector2(0, 1)
        forward_dir = dir_vector.rotate(self.rotation)
        self.position +=  forward_dir * PLAYER_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-abs(dt))

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-abs(dt))

        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.cooldown > 0:
            self.cooldown -= dt
