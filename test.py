import pygame
import time

from objects import Board, Shape, Cell

if __name__ == '__main__':
    pygame.init()
    size = X, Y = 501, 501
    screen = pygame.display.set_mode(size)

    running = True

    board = Board(10, 7, screen)
    board.set_view(50, 50, 30)

    shape = Shape([[0, 0, 1], [1, 1, 1]], (0, 255, 255), 2, (2, 3), board)
    while running:
        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        shape.update()
        board.render()
        pygame.display.flip()

        time.sleep(1)

    pygame.quit()
