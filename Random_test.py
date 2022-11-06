# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
from pygame import gfxdraw
WIDTH = 1920  # ширина игрового окна
HEIGHT = 1080 # высота игрового окна
FPS = 60 # частота кадров в секунду
# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Цикл игры
running = True
screen.fill((0,0,0))
COORDS=[]
POVT=[]
while running:
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
    coord_h = random.randrange(0,WIDTH)
    coord_w = random.randrange(0,HEIGHT)
    cor = (coord_h,coord_w)
    if cor not in COORDS:
        COORDS.append(cor)
        pygame.draw.line(screen, (0, 0, 255), (coord_h, coord_w), (coord_h, coord_w))
    else:
        POVT.append(cor)
        pygame.draw.line(screen, (255, 0, 0), (coord_h, coord_w), (coord_h, coord_w))

    print(f"Cor: {len(COORDS)}, POVT: {len(POVT)}")
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    #clock.tick(FPS)
    pygame.display.flip()
pygame.quit()