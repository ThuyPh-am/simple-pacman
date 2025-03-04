import pygame
from agents import Agent
from env import Block
from ghost import Ghost
from food import Food

pygame.init()
screen = pygame.display.set_mode((1000, 480))
clock = pygame.time.Clock()
env = Block()
agent = Agent(env)
ghost = Ghost(agent,env)
food = Food(env)
food.food_generator()

    
def eating(agent, food):
    for x,y in food.food_map:
        if -5 <= x-agent.x <= 2*food.size and -5 <= y-agent.y <= 2*food.size:
            food.food_map.remove((x,y))
    return food.food_map

def wining(agent, food):
    if len(food.food_map) == 0:
        return True
    return False

def losing(agent, ghost):
    if agent.x == ghost.x and agent.y == ghost.y:
        return True
    return False

def main():
    running = True

    while running:
        clock.tick(60)
        screen.fill((0,0,0))
        env.draw_env(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        agent.move()
        distance = ((ghost.x - agent.x) ** 2 + (ghost.y - agent.y) ** 2) ** 0.5

        if distance <= 300:
            ghost.chase()
            ghost.hit()
            if losing(agent, ghost):
                print("You lose!")
                running = False
        else: ghost.moving()

        eating(agent, food)

        if wining(agent, food):
            print("You win!")
            running = False

        agent.draw()
        ghost.draw()
        food.draw()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
