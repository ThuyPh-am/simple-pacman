import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000,480))
clock = pygame.time.Clock()

class Food:

    def __init__(self, env):
        self.size = 5
        self.color = (45, 55, 255)
        self.env = env
        self.food_map = []

    def food_generator(self):
        while True:
            x = random.randint(0, 1000)
            y = random.randint(0, 480)
            if not self.env.is_block(x, y):
                return x,y
            

    def food_load(self, num_food = 20):
        for _ in range(num_food):
            x,y = self.food_generator()
            self.food_map.append((x,y))
        
    def draw(self):
        for x,y in self.food_map:
            pygame.draw.circle(screen, self.color, (x, y), self.size)
    