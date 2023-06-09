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


fon = pygame.image.load(file_path(r"images\fon.jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT ))

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
        self.direction = "right"
        self.image_r = self.image
        self.image_l = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed_x
        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y


player = Player(5, 5, 60, 60, r"images\player.jpg", 0, 0)
enemy1 = GameSprite(100, 60, 60, 60, r"images\enemy1.png")
finish = GameSprite(200, 50, 35, 60, r"images\finish.jpg")

walls = pygame.sprite.Group()
wall1 = GameSprite(100, 300, 20, 300, r"images\OIP.jpg")
walls.add(wall1)
wall2 = GameSprite(300, 300, 300, 20, r"images\OIP.jpg")
walls.add(wall2)
wall3 = GameSprite(100, 300, 300, 20, r"images\OIP.jpg")
walls.add(wall3)

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

    clock.tick(FPS)
    pygame.display.update()