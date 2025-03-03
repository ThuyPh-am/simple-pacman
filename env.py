import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((680, 480))
clock = pygame.time.Clock()
screen.fill((0, 0, 0))

class Block:
    def __init__(self):
        self.cs50 = [" ##########   ##  #######    ###### ####    ###########",
                "#             #              #              #          ",
                "#             #                                       #",
                "              #                                       #",
                "              #              #              #         #",
                "#             ###########    ##########     #         #",
                "#                                      #    #         #",
                "#                                      #    #          ",
                "#                       #              #              ",
                "                        #              #              #",
                " ##########   ### #######    #### ######    #### ######",
                "\n",
                "\n",
                "\n"
                "###########   #########     ####### ##      ########## ",
                "#             #             #                         #",
                "#             #             #                         #",
                "#             #                             #          ",
                "#             #                             #         #",
                "#             ##########    ###########     #         #",
                "                                       #    #         #",
                "                                       #    #         #",
                "                        #              #              #",
                "#                       #              #              #",
                " ##########   ## ########    ##### #####    ##### #####"]
        
        self.x_start = 50
        self.y_start = 80
        self.block_size = 15
        self.block_grid = set() 
        self.grid_generate()

    def draw_env(self,screen):
        for y, line in enumerate(self.cs50):
            for x, char in enumerate(line):
                if char == "#":
                    pygame.draw.rect(screen, (255, 0, 0), 
                                    (self.x_start + x * self.block_size, self.y_start + y * self.block_size, 
                                    self.block_size, self.block_size))
                    
    def grid_generate(self):
        for y_idx, line in enumerate(self.cs50):
            for x_idx, char in enumerate(line):
                if char == "#":
                    block_x = self.x_start + x_idx * self.block_size
                    block_y = self.y_start + y_idx * self.block_size
                    self.block_grid.add((block_x, block_y, self.block_size, self.block_size))
        return self.block_grid


    def is_block(self, x,y,width,height):
        obj_rect = pygame.Rect(x,y, width, height)
        for block_x, block_y, block_width, block_height in self.block_grid:
            if pygame.Rect.colliderect(Rect(block_x, block_y, block_width, block_height),obj_rect):
                return True
        return False

