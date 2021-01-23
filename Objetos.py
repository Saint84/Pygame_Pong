import pygame


class Objs:
    def __init__(self, diretorio, eixo_x, eixo_y):
        self.image = pygame.image.load(diretorio)
        self.position = self.image.get_rect()
        self.position[0] = eixo_x
        self.position[1] = eixo_y

    def drawing(self, window):
        window.blit(self.image, (self.position[0], self.position[1]))
