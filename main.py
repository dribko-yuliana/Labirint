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

DARK_BLUE = (0,128,255)
LIGHT_BLUE = (51,153,255)
PURPLE = (119,51,255)
LIGHT_PURPLE = (179,102,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255,204,255)

pygame.mixer.music.load(file_path(r"music\A Few Moments Later (Spongebob) - QuickSounds.com.mp3"))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

music_shoot = pygame.mixer.Sound(file_path(r"music\bullet.ogg"))
music_shoot.set_volume(0.50)


fon = pygame.image.load(file_path(r"images\OIP (1).jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT ))

image_win = pygame.image.load(file_path(r"images\win.jpg"))
image_win = pygame.transform.scale(image_win, (WIN_WIDTH, WIN_HEIGHT))

image_lose = pygame.image.load(file_path(r"images\lose.jpg"))
image_lose = pygame.transform.scale(image_lose, (WIN_WIDTH, WIN_HEIGHT))


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class Button():
    def __init__(self, x, y, width, height, color1, color2, text, shrift_fon, text_color, text_x, text_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        shrift = pygame.font.SysFont(shrift_fon, 20)
        self.text = shrift.render(text, True, text_color)
        self.text_x = text_x
        self.text_y = text_y
   
    def show(self):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text, (self.rect.x + self.text_x, self.rect.y + self.text_y)) 


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

    def shoot(self):
        if self.direction == "right":
            bullet = Bullet(self.rect.right, self.rect.centery, 40, 40, r"images\download.png", 5)
        elif self.direction == "left":
            bullet = Bullet(self.rect.left - 40, self.rect.centery, 40, 40, r"images\download.png", -5 )
            bullet.image = pygame.transform.flip(bullet.image, True, False)
        bullets.add(bullet)


    def update(self):
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed_x
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)
        if self.speed_x < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)


        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y

        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_y < 0:
            for wall in walls_touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)
        if self.speed_y > 0:
            for wall in walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)

class Bullet(GameSprite):
    def __init__(self, x , y, width, height, image, speed):
        super().__init__(x, y, width, height, image)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIN_WIDTH or self.rect.left <= 0:
            self.kill()




class Enemy(GameSprite):
    def __init__ (self, x , y, width, height, image, direction, min_coord, max_coord, speed):
        super().__init__(x , y, width, height, image)
        self.direction = direction
        self.min_coord = min_coord
        self.max_coord = max_coord
        self.speed = speed

        if self.direction == "left":
            self.image_l = self.image
            self.image_r = pygame.transform.flip(self.image, True, False)
        elif self.direction == "right":
            self.image_r = self.image
            self.image_l = pygame.transform.flip(self.image, True, False)


    def update(self):
        if self.direction == "left" or self.direction == "right":
            if self.direction == "left":
                self.rect.x -= self.speed

            elif self.direction == "right":
                self.rect.x += self.speed

            if self.rect.right >= self.max_coord:
                self.direction = "left"
                self.image = self.image_r
            if self.rect.left <= self.min_coord:
                self.direction = "right"
                self.image = self.image_l


        elif self.direction == "up" or self.direction == "down":
            if self.direction == "up":
                self.rect.y -= self.speed
            elif self.direction == "down":
                self.rect.y += self.speed

            if self.rect.top <= self.min_coord:
                self.direction = "down"
            if self.rect.bottom >= self.max_coord:
                self.direction = "up"

        



player = Player(5, 5, 60, 60, r"images\player.png", 0, 0)
finish = GameSprite(120, 60, 60, 70, r"images\finish.png")

enemies = pygame.sprite.Group()
enemy1 = Enemy(300, 215, 60, 60, r"images\enemy1.png", "right", 300, 550, 4)
enemy2 = Enemy(700, 400, 60, 90, r"images\enemy2.png", "down", 200, 600, 3)
enemy3 = Enemy(200, 300, 70, 80, r"images\enemy3.png", "right", 100, 430, 7)
enemies.add(enemy1)
enemies.add(enemy2)
enemies.add(enemy3)

bullets = pygame.sprite.Group()



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
wall27 = GameSprite(80, 0, 20, 120, r"images\fon.jpg")
walls.add(wall27)


btn_start = Button(200, 300, 150, 60, DARK_BLUE, LIGHT_BLUE, "START", "Arial",BLACK, 40, 20)
btn_exit = Button(420, 300, 150, 60, PURPLE, LIGHT_PURPLE, "EXIT", "Arial", BLACK, 40, 20)
game_name = pygame.font.SysFont("Arial", 50, 1).render("SPONGE BOB SQUARE PANTS", True, BLACK)

level = 0
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if level == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = -5
                    player.direction = "left"
                    player.image = player.image_l
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 5
                    player.direction = "right"
                    player.image = player.image_r
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = -5
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    music_shoot.play(1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = 0

        elif level == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    level = 1
                    pygame.mixer.music.load(file_path(r"music\Spongebob_Squarepants_The_Yellow_Album_13_Jelly_Fish_Jam.mp3"))
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(-1)
                elif btn_exit.rect.collidepoint(x, y):
                    game = False

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    btn_start.color = btn_start.color2

                elif btn_exit.rect.collidepoint(x, y):
                    btn_exit.color = btn_start.color2

                else:
                    btn_start.color = btn_start.color1
                    btn_exit.color = btn_exit.color1

    if level == 1:
        window.blit(fon, (0, 0))
        walls.draw(window)
        player.show()
        player.update()
        enemies.draw(window)
        enemies.update()
        finish.show()
        bullets.draw(window)
        bullets.update()
    
        if pygame.sprite.collide_rect(player, finish):
            level = 10
            pygame.mixer.music.stop()
            pygame.mixer.music.load(file_path(r"music\Spongebob_Ravioli_Ravioli_Give_Me_the_Formuoli_QuickSounds_com.mp3"))
            pygame.mixer.music.play(-1)

        if pygame.sprite.spritecollide(player, enemies, False):
            level = 11 
            pygame.mixer.music.stop()
            pygame.mixer.music.load(file_path(r"music\A Few Moments Later (Spongebob) - QuickSounds.com.mp3"))
            pygame.mixer.music.play(-1)

        pygame.sprite.groupcollide(bullets, walls, True, False)
        pygame.sprite.groupcollide(bullets, enemies, True, True)

    elif level == 0:
        window.fill(PINK)
        btn_start.show()
        btn_exit.show()
        window.blit(game_name, (25, 30))

    elif level == 10:
        window.blit(image_win, (0, 0))

    elif level == 11:
        window.blit(image_lose, (0, 0))


    clock.tick(FPS)
    pygame.display.update()