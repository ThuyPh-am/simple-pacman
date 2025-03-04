import pygame
from env import Block

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Agent:

    def __init__(self, env):
        self.x = 50
        self.y = 50
        self.vel = 3
        self.width = 10
        self.height = 10
        self.color = (0,0,255)
        self.env = env

    def move(self):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y
        if keys[pygame.K_LEFT] and self.x > self.vel:
            new_x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 1000 - self.width:
            new_x += self.vel
        if keys[pygame.K_UP]  and self.y > self.vel:
            new_y -= self.vel
        if keys[pygame.K_DOWN] and self.y < 480 - self.height:
            new_y += self.vel

        if not self.env.is_block(new_x, new_y, self.width, self.height):
            self.x = new_x
            self.y = new_y
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    