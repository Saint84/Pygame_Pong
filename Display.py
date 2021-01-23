import pygame


class Window:
    def __init__(self, x, y, title):
        pygame.init()
        self.window = pygame.display.set_mode([x, y])
        self.title = pygame.display.set_caption(title)
        self.list_obj = []
        self.loop = True

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def add_obj(self, item):
        self.list_obj.append(item)

    def update(self):
        while self.loop:
            self.events()
            pygame.display.update()
