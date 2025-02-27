import pygame
from agents import Agent
from env import Block
from ghost import Ghost

pygame.init()
screen = pygame.display.set_mode((1000, 480))
clock = pygame.time.Clock()

def main():
    env = Block()
    agent = Agent(env)
    ghost = Ghost(agent,env)


    running = True

    while running:
        clock.tick(60)
        screen.fill((0,0,0))
        env.draw_env(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        agent.move()
        ghost.chase()
        ghost.hit()

        agent.draw()
        ghost.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()
