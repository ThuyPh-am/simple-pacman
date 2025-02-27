import pygame
from env import Block

pygame.init()
screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()


class Ghost:

    def __init__(self,agent, env):
        self.x = 20
        self.y = 20
        self.vel_chase = 3
        self.vel_normal = 2
        self.width = 10
        self.height = 10
        self.color = (0,255,0)
        self.agent = agent
        self.env = env


    def moving(self):
        if self.x < 900 and not self.env.is_block(self.x-self.vel_normal, self.y):
            self.x += self.vel_normal 
        else:
            self.x = 10 # reset position in edge case

    def chase(self):
        """
        finding agent x and y and follow by vel_chase 
        """
        if self.agent.x < self.x and not self.env.is_block(self.x - self.vel_chase, self.y):
            self.x -= self.vel_chase
        elif self.agent.y < self.y and not self.env.is_block(self.x, self.y-self.vel_chase):
            self.y -= self.vel_chase
        elif self.agent.x > self.x and not self.env.is_block(self.x + self.vel_chase, self.y):
            self.x += self.vel_chase
        elif self.agent.y > self.y and not self.env.is_block(self.x, self.y + self.vel_chase):
            self.y += self.vel_chase

    def hit(self):
        if self.agent.x == self.x and self.agent.y == self.y:
            self.agent.x =0
            self.agent.y = 0


    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))        

# def main():
#     running = True
#     agent = Agent()
#     ghost = Ghost(agent)

#     while running:
#         clock.tick(60)
#         screen.fill((0,0,0))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         agent.move()
#         ghost.chase()
#         ghost.moving()

#         ghost.draw()
#         agent.draw()

#         pygame.display.flip()

# if __name__ == "__main__":
#     main()