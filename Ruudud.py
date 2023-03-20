# Impordib Pygame moodul
import pygame

# Initsialiseerib Pygame
pygame.init()
pygame.display.set_mode((640, 480))

# Defineeri akna suurus ja pealkirja
width = 640
height = 480
title = "Ruudustiku Joonistamise Programm"
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

# Kasutaja sisestab andmed
cube_size = int(input("Sisesta iga ruudu suurus (pikslites): "))
num_rows = int(input("Sisesta ridade arv: "))
num_cols = int(input("Sisesta veergude arv: "))
line_color_input = input("Sisesta joonte värv (RGB väärtused komadega eraldatult, nt 255,0,0 punase jaoks): ")
line_color = tuple(map(int, line_color_input.split(",")))

# Arvutab ruudu suuruse, et see kataks terve ekraani
cube_size_x = width // num_cols
cube_size_y = height // num_rows

# Vaatab, et mäng töötaks
running = True
while running:
    # Kontrollib sündmusi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Sulgeb mängu kui ristist kinna panna
            running = False

    # Täidab ekraan taustavärviga
    screen.fill((152, 251, 152))

    # Joonistab ruudustiku
    for x in range(0, num_cols * cube_size_x, cube_size_x):
        pygame.draw.line(screen, line_color, (x, 0), (x, height), 2)
    for y in range(0, num_rows * cube_size_y, cube_size_y):
        pygame.draw.line(screen, line_color, (0, y), (width, y), 2)

    # Uuendab ekraani
    pygame.display.update()

# Paneb mängu kinni.
pygame.quit()