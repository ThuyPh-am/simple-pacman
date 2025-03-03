import pytest
from project import eating , losing, wining
from agents import Agent
from food import Food
from ghost import Ghost
from env import Block
import pygame

@pytest.fixture
def setup():
    # pygame.init()
    # screen = pygame.display.set_mode((680, 480))
    # clock = pygame.time.Clock()
    # screen.fill((0, 0, 0))
    wall = Block()
    agent = Agent(wall)
    food = Food(wall)
    ghost = Ghost(agent, wall)
    food.food_map = [(50, 80), (100, 100), (150, 150), (200, 200)]
    food.size = 5
    return wall, agent, food, ghost

def test_eating(setup):
    wall, agent, food, ghost = setup
    agent.x = 100
    agent.y = 100
    eated_food_map = eating(agent, food)
    assert (50,80) in eated_food_map
    assert (100,100) not in eated_food_map

def test_wining(setup):
    wall, agent, food, ghost = setup
    pos = [(50, 80),(100,100),(150, 150), (200, 200)]
    for x,y in pos:
        agent.x , agent.y = x, y
        eaten_food_map = eating(agent, food)
        food.food_map = eaten_food_map
    assert len(food.food_map) == 0
    assert wining(agent, food) == True


def test_losing(setup):
    wall, agent, food, ghost = setup
    agent.x = 100
    agent.y = 100
    ghost.x = 100
    ghost.y = 100
    assert losing(agent, ghost) == True