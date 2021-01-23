from Display import Window
from Objetos import Objs


class Game:
    def __init__(self):
        self.tela = Window(1280, 720, "Pong Fut")

        self.background = Objs("assets/field.png", 0, 0)
        self.tela.add_obj(self.background.drawing(self.tela.window))

        self.player01 = Objs("assets/player1.png", 50, 310)
        self.tela.add_obj(self.player01.drawing(self.tela.window))

        self.player02 = Objs("assets/player2.png", 1150, 310)
        self.tela.add_obj(self.player02.drawing(self.tela.window))

        self.ball = Objs("assets/ball.png", 617, 337)
        self.tela.add_obj(self.ball.drawing(self.tela.window))


Game().tela.update()
