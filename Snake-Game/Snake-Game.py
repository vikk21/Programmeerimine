import pygame # impordib pygame'i mooduli
import time # impordib aja'i mooduli
import random # impordib randomi mooduli

pygame.init() # initsialiseerib pygame'i

white = (255, 255, 255) # defineerib värvi
yellow = (255, 255, 102) # defineerib värvi
black = (0, 0, 0) # defineerib värvi
red = (213, 50, 80) # defineerib värvi
green = (0, 255, 0) # defineerib värvi
blue = (50, 153, 213) # defineerib värvi

dis_width = 640 # defineerib akna laiuse
dis_height = 640 # defineerib akna kõrguse

dis = pygame.display.set_mode((dis_width, dis_height)) # loob pygame'i akna
pygame.display.set_caption('Snake Game') # seab pealkirja aknale
pygame.mixer.music.load('MainMusic.mp3') # laeb muusikapala mängu jaoks
pygame.mixer.music.play(0) # esitab muusikapala

clock = pygame.time.Clock() # defineerib kella pygame'i jaoks

snake_block = 10 # defineerib mao bloki suuruse
snake_speed = 15 # defineerib mao liikumiskiiruse

font_style = pygame.font.SysFont("bahnschrift", 25) # seab fondi stiili
score_font = pygame.font.SysFont("comicsansms", 35) # seab fondi stiili

def Your_score(score): # funktsioon skoori näitamiseks
    value = score_font.render("Your Score: " + str(score), True, yellow) # seab väärtuse skoori jaoks
    dis.blit(value, [0, 0]) # kuvab skoori


def our_snake(snake_block, snake_list): # funktsioon mao joonistamiseks
    for x in snake_list: # läheb läbi madu moodustavate blokkide loendi
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block]) # joonistab mao bloki


def message(msg, color): # funktsioon sõnumite kuvamiseks
    mesg = font_style.render(msg, True, color) # seab väärtuse sõnumi jaoks
    dis.blit(mesg, [dis_width / 6, dis_height / 3]) # kuvab sõnumi aknal


def gameLoop(): # funktsioon mängu tsükli jaoks
    game_over = False # seab mängu lõppemise muutuja valeks
    game_close = False # seab mängu sulgemise muutuja valeks

    x1 = dis_width / 2 # määrab akna laiuse
    y1 = dis_height / 2 # määrab akna kõrguse

    x1_change = 0 # määrab muutuja väärtuseks nulli
    y1_change = 0 # määrab muutuja väärtuseks nulli

    snake_List = [] # loob kasti kuhu saab ussi lisada
    Length_of_snake = 1 # ussi pikkus


    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # genereerib ussi kuubiku suvalisse kohta
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 # genereerib ussi kuubiku suvalisse kohta

    while not game_over: # kuniks mäng pole läbi

        # Kui mängija kaotab
        while game_close == True:
            # Lõpetab mängumuusika mängimise, täidab tausta sinise värviga ning kuvab sõnumi
            pygame.mixer.music.stop()
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.mixer.music.play(0)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Võtab sündmused pygame'i sündmuste järjekorrast
            for event in pygame.event.get():
                # Kui kasutaja vajutab sulgemisnuppu, lõpetab mängu
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                # Kui kasutaja vajutab Q, lõpetab mängu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    # Kui kasutaja vajutab C, alustab mäng uuesti
                    if event.key == pygame.K_c:
                        gameLoop()

        # Võtab sündmused pygame'i sündmuste järjekorrast
        for event in pygame.event.get():
            # Kui kasutaja vajutab sulgemisnuppu, lõpetab mängu
            if event.type == pygame.QUIT:
                game_over = True
            # Kui kasutaja vajutab noolenuppu vasakule, muudab ussi suunda vastavalt x-teljele
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                # Kui kasutaja vajutab noolenuppu paremale, muudab ussi suunda vastavalt x-teljele
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                # Kui kasutaja vajutab noolenuppu ülespoole, muudab ussi suunda vastavalt y-teljele
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                # Kui kasutaja vajutab noolenuppu alla, muudab ussi suunda vastavalt y-teljele
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Kontrollib, kas madu puutub kokku seina või ekraani servaga
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Liigutab madu koordinaatide järgi
        x1 += x1_change
        y1 += y1_change

        # loob tausta ning lisab selle sinna
        background = pygame.image.load("background_dirt.jpg")
        # tausta mõõtmed
        background = pygame.transform.scale(background, [640, 640])
        # lisab tausta mänguväljale
        dis.blit(background, [0, 0])

        # joonistab toidu, kasutades sinist värvi
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        # lisab madu pea koordinaadid listi ja kustutab vajadusel madu saba
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # kontrollib, kas madu sattus iseendaga kokku
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # joonistab mado mänguväljale
        our_snake(snake_block, snake_List)
        # kuvab mängija skoori
        Your_score(Length_of_snake - 1)

        # värskendab ekraani
        pygame.display.update()

        # Kui madu sööb toidu, siis toidu asukoht muutub ja madu pikeneb
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Reguleerib mängu kiirust
        clock.tick(snake_speed)

    # Lõpetab pygame'i töö ja sulgeb akna
    pygame.quit()
    quit()

# Käivitab mängu uuesti
gameLoop()