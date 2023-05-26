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

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

level = 1

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if level == 1:
        pass

    clock.tick(FPS)
    pygame.display.update()