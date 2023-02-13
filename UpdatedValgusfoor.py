import pygame #impordib pygame
pygame.init() #Koostab selle programmi
#ekraani seaded
screen=pygame.display.set_mode([300,700]) #valib ekraani suuruse
pygame.display.set_caption("Valgusfoor") #Lisab aknale nime

#joonistamine
pygame.draw.rect(screen, [255, 255, 255], [90, 10, 130, 280], 2) #loob ristküliku [värv], [[x, y, w, h], joone_paksus)
pygame.draw.circle(screen, [255, 0, 0], [155,63], 40, 0) #loob ringi [värv] ,[(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.circle(screen, [236, 240, 0], [155,152], 40, 0) #loob ringi [värv] ,[(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.circle(screen,[0, 255, 0], [155,240], 40, 0) #loob ringi [värv] ,[(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.line(screen, [255,255,255], [155,290], [155,500], 2)
pygame.draw.polygon(screen, [0, 0, 0] , [[90,500],[220,500],[290,600],[10,600],[90,500]], 2) #Värv ja Hulknurga ehk polygon-i mõõtmed.
pygame.draw.polygon(screen, [0, 123, 255], [[90,500],[220,500],[243,533],[64,533],[90,500]], 0) 
pygame.draw.polygon(screen, [0, 0, 0], [[64,533],[243,533],[266,566],[38,566],[64,533]], 0) 
pygame.draw.polygon(screen, [255, 255, 255], [[38,566],[266,566],[290,600],[10,600],[38,566]], 0) 
pygame.display.flip() #värskendab aknaid
running = True #Hoiab programmi tööle

while running: #Loop
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get(): # Käivitab mooduli mis sulgeb akna
        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
   
pygame.quit()
