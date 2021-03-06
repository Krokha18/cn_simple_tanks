import pygame
class Bullet():
    def __init__(self, x, y,direction ,color ):
        # центр шарика
        self.x = x
        self.y = y
        # радиус
        self.r = 10
        self.color = color
        # направление, скорость
        self.direction = direction
        self.vel = 3 #1

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r )

    def move(self):
        keys = pygame.key.get_pressed()
        # обработка нажатой клавиши
        if self.direction == 1:
            self.x -= self.vel

        if self.direction == 3:
            self.x += self.vel

        if self.direction == 4:
            self.y -= self.vel

        if self.direction == 2:
            self.y += self.vel
