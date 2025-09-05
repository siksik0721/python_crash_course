import sys

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((100, 100, 255))
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
