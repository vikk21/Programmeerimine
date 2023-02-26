import pygame
import random

# Alustab pygame'iga
pygame.init()

# Määrab ekraani suuruse
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Loob akna nime
pygame.display.set_caption("Automäng")

# Laeb pildid
red_car_img = pygame.image.load("red_car.png").convert_alpha()
blue_car_img = pygame.image.load("blue_car.png").convert_alpha()
cover_photo = pygame.image.load("cover_photo.jpg").convert_alpha()

# Punase auto positsioon
red_car_width, red_car_height = red_car_img.get_size()
red_car_x = screen_width / 2 - red_car_width / 2
red_car_y = screen_height - red_car_height

# Sinise auto muutujad
blue_car_width, blue_car_height = blue_car_img.get_size()
blue_car_x = random.randint(0, screen_width - blue_car_width)
blue_car_y = -blue_car_height
blue_car_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Tee kiirus
road_y = 0
road_speed = 7
road_width = cover_photo.get_width()
road_height = cover_photo.get_height()

# Tsükli kordumine
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Punase auto liikumine
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        red_car_x -= 5
    if keys[pygame.K_d]:
        red_car_x += 5

    # Punane auto jääb piiridesse
    if red_car_x < 0:
        red_car_x = 0
    elif red_car_x > screen_width - red_car_width:
        red_car_x = screen_width - red_car_width

    # Sinise auto liikumine
    blue_car_y += blue_car_speed
    if blue_car_y > screen_height:
        blue_car_y = -blue_car_height
        blue_car_x = random.randint(0, screen_width - blue_car_width)
        score += 1
        blue_car_speed += 0.5

    # Tee liikumine
    road_y += road_speed
    if road_y > road_height:
        road_y -= road_height

    # Kontrollib kas punane auto põrkas kokku sinisega
    if red_car_x < blue_car_x + blue_car_width and \
            red_car_x + red_car_width > blue_car_x and \
            red_car_y < blue_car_y + blue_car_height and \
            red_car_y + red_car_height > blue_car_y:
        running = False

    # Taust ja autode joonistamine
    screen.blit(cover_photo, (0, road_y - road_height))
    screen.blit(cover_photo, (0, road_y))
    screen.blit(red_car_img, (red_car_x, red_car_y))
    screen.blit(blue_car_img, (blue_car_x, blue_car_y))

    # Skiiri joonistamine
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Värskendab ekraani
    pygame.display.update()

    # Frame rate piirang
    clock.tick(60)

# Paneb mängu kinni
pygame.quit()