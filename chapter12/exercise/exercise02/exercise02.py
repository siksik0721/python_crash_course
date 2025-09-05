import sys

import pygame

from boss import Boss


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))

        self.boss = Boss(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((255, 255, 255))
            self.boss.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
