import pygame


class Player():
    def __init__(self, x, y, h1, h2 ,h3, health):
        #координаты
        self.x = x
        self.y = y
        self.health = health
        #ширина-высота
        self.width = 50
        self.height = 50
        self.color = (h1, h2, h3)
        self.rect = (x,y,self.width,self.height)
        #скорость передвижения за одно нажатие
        self.vel = 2

    def draw(self, win):
        #отрисовка игрока
        pygame.draw.rect(win, self.color, self.rect)

    def move(self, width, height):
        keys = pygame.key.get_pressed()
        #считали нажатую клавишу(вверх вниз вправо влево) и передвинули игрока)
        if(( keys[pygame.K_LEFT] ) and (self.x - self.vel > 0)):
            self.x -= self.vel

        if(( keys[pygame.K_RIGHT]) and (self.x+self.vel < width)):
            self.x += self.vel

        if(( keys[pygame.K_UP] ) and (self.y - self.vel > 0)):
            self.y -= self.vel

        if(( keys[pygame.K_DOWN]) and (self.y + self.vel < height)):
            self.y += self.vel


        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
