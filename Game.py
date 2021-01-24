import pygame


class Game:
    def __init__(self):
        pygame.display.set_caption("Pong - Pong - Inicializado")
        self.window = pygame.display.set_mode([1280, 720])

        self.background = pygame.image.load("assets/field.png")
        self.ball = pygame.image.load("assets/ball.png")
        self.player01 = pygame.image.load("assets/player1.png")
        self.player02 = pygame.image.load("assets/player2.png")
        self.score01 = pygame.image.load(f"assets/score/0.png")
        self.score02 = pygame.image.load(f"assets/score/0.png")
        self.win = pygame.image.load(f"assets/win.png")

        self.c_x = -5
        self.c_y = 6
        self.ball_x = 617
        self.ball_y = 337
        self.player01_x = 50
        self.player01_y = 310
        self.player02_x = 1150
        self.player02_y = 310
        self.player01_moveup = False
        self.player01_movedown = False
        self.score_player01 = 0
        self.score_player02 = 0

        self.loop = True

    def drawing(self, window):
        window.blit(self.background, (0, 0))
        window.blit(self.ball, (self.ball_x, self.ball_y))
        window.blit(self.player01, (self.player01_x, self.player01_y))
        window.blit(self.player02, (self.player02_x, self.player02_y))
        window.blit(self.score01, (550, 50))
        window.blit(self.score02, (660, 50))

    def move_ball(self):
        self.ball_x += self.c_x
        self.ball_y -= self.c_y

        if self.ball_x < - 50:
            self.ball_x = 617
            self.ball_y = 337
            self.c_x *= -1.1
            self.c_y *= -1.1
            self.score_player02 += 1

        if self.ball_x > 1300:
            self.ball_x = 617
            self.ball_y = 337
            self.c_x *= -1.1
            self.c_y *= -1.1
            self.score_player01 += 1

        if (self.ball_y > 685) or (self.ball_y < 25):
            self.c_y *= -1

    def colide_box(self):
        if self.ball_x < 123:
            if (self.player01_y <= self.ball_y + 23) and (self.player01_y + 146 >= self.ball_y):
                self.c_x *= -1
        if self.ball_x > 1100:
            if (self.player02_y <= self.ball_y + 23) and (self.player02_y + 146 >= self.ball_y):
                self.c_x *= -1

    def move_player01(self):
        if self.player01_moveup:
            self.player01_y -= 10
        if self.player01_movedown:
            self.player01_y += 10
        if self.player01_y <= 0:
            self.player01_y = 0
        if self.player01_y >= 575:
            self.player01_y = 575

    def move_player02(self):
        self.player02_y = self.ball_y
        if self.player02_y <= 0:
            self.player02_y = 0
        if self.player02_y >= 575:
            self.player02_y = 575

    def event(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_s:
                    self.player01_movedown = True
                if events.key == pygame.K_w:
                    self.player01_moveup = True
            if events.type == pygame.KEYUP:
                if events.key == pygame.K_s:
                    self.player01_movedown = False
                if events.key == pygame.K_w:
                    self.player01_moveup = False

    def update(self):
        while self.loop:
            if self.score_player02 < 9:
                self.drawing(self.window)
                self.move_ball()
                self.colide_box()
                self.event()
                self.move_player01()
                self.move_player02()
                pygame.display.update()
                self.score01 = pygame.image.load(f"assets/score/{self.score_player01}.png")
                self.score02 = pygame.image.load(f"assets/score/{self.score_player02}.png")
            else:
                self.drawing(self.window)
                self.event()
                self.window.blit(self.win, (300, 330))
                pygame.display.update()


Game().update()
