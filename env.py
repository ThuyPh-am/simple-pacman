import pygame

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
        
        #starting position
        self.x_start = 50
        self.y_start = 80

        self.block_size = 15

    def draw_env(self,screen):
        for y, line in enumerate(self.cs50):
            for x, char in enumerate(line):
                if char == "#":
                    pygame.draw.rect(screen, (255, 0, 0), 
                                    (self.x_start + x * self.block_size, self.y_start + y * self.block_size, 
                                    self.block_size, self.block_size))
                    
    def is_block(self, obj_x, obj_y):
        for y_idx, line in enumerate(self.cs50):
            for x_idx, char in enumerate(line):
                if char == "#":
                    block_x = self.x_start + x_idx * self.block_size
                    block_y = self.y_start + y_idx * self.block_size

                    if block_x <= obj_x <= block_x + self.block_size and block_y <= obj_y <= block_y + self.block_size:
                        return True
        return False

# def main():
#     running = True
#     draw_env()

#     while running:
#         clock.tick(60)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#     pygame.quit()


# if __name__ == "__main__":
#     main()