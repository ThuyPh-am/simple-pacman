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

    def food_generator(self, num_food = 20, max_attemps = 1000):
        self.food_map = []
        for _ in range(num_food):
            for _ in range(max_attemps):
                x = random.randint(50, 800)
                y = random.randint(80, 400)
                if not self.env.is_block(x, y, self.size, self.size):
                    self.food_map.append((x, y))
                    break


    def draw(self):
        for x,y in self.food_map:
            pygame.draw.circle(screen, self.color, (x, y), self.size)
    