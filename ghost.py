import pygame
from env import Block
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()


class Ghost:

    def __init__(self,agent, env):
        self.x = 20
        self.y = 20
        self.vel_chase = 2
        self.vel_normal = 1
        self.width = 10
        self.height = 10
        self.color = (0,255,0)
        self.agent = agent
        self.env = env


    def moving(self):
        if self.x < 900 and not self.env.is_block(self.x + self.vel_normal, self.y, self.width, self.height):
                self.x += self.vel_normal
        elif self.y < 400 and not self.env.is_block(self.x, self.y + self.vel_normal, self.width, self.height): 
                self.y += self.vel_normal
        elif self.x > 10 and not self.env.is_block(self.x - self.vel_normal, self.y, self.width, self.height):
                self.x -= self.vel_normal
        elif self.y > 10 and not self.env.is_block(self.x, self.y - self.vel_normal, self.width, self.height):
                self.y -= self.vel_normal
        else: self.x = 10 # reset position in edge case

    def chase(self):
        """
        finding agent x and y and follow by vel_chase 
        """
        new_x, new_y = self.x , self.y
        if self.agent.x < self.x:
            new_x-= self.vel_chase
        elif self.agent.y < self.y:
            new_y -= self.vel_chase
        elif self.agent.x > self.x:
            new_x += self.vel_chase
        elif self.agent.y > self.y:
            new_y += self.vel_chase

        if not self.env.is_block(new_x, new_y, self.width, self.height):
            self.x = new_x
            self.y = new_y

    def hit(self):
        if self.agent.x == self.x and self.agent.y == self.y:
            return True
        return False


    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height)) 