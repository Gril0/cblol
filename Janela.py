import sys
from PyQt5 import QtWidgets
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

def window():
    app = QtWidgets.QApplication(sys.argv)

    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('CBLOL SIMULATOR')
    clock = pygame.time.Clock()
    background_position = [0, 0]
    background_image = pygame.image.load("imagens/teste.jpg").convert()
    screen.blit(background_image, background_position)
    pygame.display.flip()
    clock.tick(60)
    sys.exit(app.exec_())

pygame.quit()
