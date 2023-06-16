import pygame
import os
pygame.init()

def file_path(filename):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, filename)
    return path

WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 40


fon = pygame.image.load(file_path(r"images\background.jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT ))

image_win = pygame.image.load(file_path(r"images\fon.jpg"))
image_win = pygame.transform.scale(image_win, (WIN_WIDTH, WIN_HEIGHT))

image_lose = pygame.image.load(file_path(r"images\background.jpg"))
image_lose = pygame.transform.scale(image_lose, (WIN_WIDTH, WIN_HEIGHT))


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x , y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__ (self, x , y, width, height, image, speed_x, speed_y):
        super().__init__(x , y, width, height, image)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction = "left"
        self.image_l = self.image
        self.image_r = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed_x
        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y


player = Player(5, 5, 60, 60, r"images\player.png", 0, 0)
enemy1 = GameSprite(100, 60, 60, 60, r"images\enemy1.png")
finish = GameSprite(200, 50, 35, 60, r"images\finish.png")

walls = pygame.sprite.Group()
wall1 = GameSprite(80, 500, 20, 150, r"images\fon.jpg")
walls.add(wall1)
wall2 = GameSprite(200, 500, 150, 20, r"images\fon.jpg")
walls.add(wall2)
wall3 = GameSprite(80, 400, 275, 20, r"images\fon.jpg")
walls.add(wall3)
wall4 = GameSprite(340, 400, 20, 120, r"images\fon.jpg")
walls.add(wall4)
wall5 = GameSprite(80, 100, 20, 200, r"images\fon.jpg")
walls.add(wall5)
wall6 = GameSprite(80, 80, 120, 20, r"images\fon.jpg")
walls.add(wall6)
wall7 = GameSprite(300, 0, 20, 120, r"images\fon.jpg")
walls.add(wall7)
wall8 = GameSprite(300, 100, 20, 120, r"images\fon.jpg")
walls.add(wall8)
wall9 = GameSprite(200, 200, 120, 20, r"images\fon.jpg")
walls.add(wall9)
wall10 = GameSprite(100, 280, 120, 20, r"images\fon.jpg")
walls.add(wall10)
wall11 = GameSprite(220, 280, 120, 20, r"images\fon.jpg")
walls.add(wall11)
wall12 = GameSprite(340, 280, 120, 20, r"images\fon.jpg")
walls.add(wall12)
wall13 = GameSprite(440, 280, 20, 120, r"images\fon.jpg")
walls.add(wall13)
wall14 = GameSprite(440, 400, 20, 120, r"images\fon.jpg")
walls.add(wall14)
wall15 = GameSprite(580, 500, 120, 20, r"images\fon.jpg")
walls.add(wall15)
wall16 = GameSprite(560, 500, 20, 120, r"images\fon.jpg")
walls.add(wall16)
wall17 = GameSprite(460, 390, 120, 20, r"images\fon.jpg")
walls.add(wall17)
wall18 = GameSprite(560, 390, 120, 20, r"images\fon.jpg")
walls.add(wall18)
wall19 = GameSprite(660, 280, 20, 120, r"images\fon.jpg")
walls.add(wall19)
wall20 = GameSprite(560, 280, 120, 20, r"images\fon.jpg")
walls.add(wall20)
wall21 = GameSprite(540, 180, 20, 120, r"images\fon.jpg")
walls.add(wall21)
wall22 = GameSprite(540, 100, 20, 120, r"images\fon.jpg")
walls.add(wall22)
wall23 = GameSprite(560, 100, 120, 20, r"images\fon.jpg")
walls.add(wall23)
wall24 = GameSprite(435, 100, 120, 20, r"images\fon.jpg")
walls.add(wall24)
wall25 = GameSprite(435, 100, 20, 120, r"images\fon.jpg")
walls.add(wall25)
wall26 = GameSprite(700, 190, 120, 20, r"images\fon.jpg")
walls.add(wall26)

level = 1
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if level == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = -5
                    player.direction = "right"
                    player.image = player.image_r
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 5
                    player.direction = "left"
                    player.image = player.image_l
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = 0

    if level == 1:
        window.blit(fon, (0, 0))
        walls.draw(window)
        player.show()
        player.update()
        enemy1.show()
        finish.show()

        if pygame.sprite.collide_rect(player, finish):
            level = 10
    
    elif level == 10:
        window.blit(image_win, (0, 0))

    clock.tick(FPS)
    pygame.display.update()