# refer to Tech With Tim
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
        if keys[pygame.K_LEFT] and self.x > self.vel and not self.env.is_block(self.x-self.vel, self.y):
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 1000 - self.width - self.vel and not self.env.is_block(self.x + self.vel, self.y):
            self.x += self.vel
        if keys[pygame.K_UP]  and self.y > self.vel and not self.env.is_block(self.x, self.y - self.vel):
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < 480 - self.height - self.vel and not self.env.is_block(self.x, self.y + self.vel):
            self.y += self.vel
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    # def jump(self):
    #     keys = pygame.key.get_pressed()
    #     if self.is_jumping:
    #         if self.jump_count >= -10:
    #             neg = 1
    #             if self.jump_count < 0:
    #                 neg = -1
    #             self.y -= (self.jump_count ** 2) * 0.5 * neg
    #             self.jump_count -= 1
    #         else:
    #             self.is_jumping = False
    #             self.jump_count = 10

    #     elif keys[pygame.K_SPACE]:
    #         self.is_jumping = True 

        

# def main():
#     running = True
#     player= Agent()
    
#     while running:
#         clock.tick(60)
#         screen.fill((0,0,0))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
        
#         player.move()
#         player.jump()
#         player.draw()

#         pygame.display.flip()

# if __name__ == "__main__":
#     main()
