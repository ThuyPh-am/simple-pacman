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
                x = random.randint(0, 980)
                y = random.randint(0, 480)
                if not self.env.is_block(x, y):
                    self.food_map.append((x, y))
                    break
    
    def eating(self, obj_x, obj_y):
        for x,y in self.food_map:
            if -5 <= x-obj_x <= 2*self.size and -5 <= y-obj_y <= 2*self.size:
                # print (f" Position of food:{x},{y} and position of agent {obj_x}, {obj_y}")
                self.food_map.remove((x,y))
                return True

    def draw(self):
        for x,y in self.food_map:
            pygame.draw.circle(screen, self.color, (x, y), self.size)
    