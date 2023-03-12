import pygame
pygame.init()

# Kuvab ekraaniseaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping-Pong")
screen.fill((200, 200, 200))

# Palli seaded
ballImg = pygame.image.load('ball.png').convert_alpha()
ballRect = ballImg.get_rect(center=(screenX // 2, screenY // 2))
ballSpeedX = 5
ballSpeedY = 5

# Aluse seaded
paddleImg = pygame.image.load('pad.png').convert_alpha()
paddleWidth = 120
paddleHeight = 20
paddleImg = pygame.transform.scale(paddleImg, (paddleWidth, paddleHeight))
paddleRect = paddleImg.get_rect(center=(screenX // 2, int(screenY / 1.5)))
paddleSpeed = 7

# Skoori seaded
scoreFont = pygame.font.Font(None, 36)

# Skoori ühikud
score = 0

# Loop
clock = pygame.time.Clock()
gameOver = False
while not gameOver:
    clock.tick(60)

    # Hoiab mängu töös
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # Liigutab palli
    ballRect.x += ballSpeedX
    ballRect.y += ballSpeedY

    # Kontrollib kas pall on vastu seina läinud
    if ballRect.left < 0 or ballRect.right > screenX:
        ballSpeedX = -ballSpeedX
    if ballRect.top < 0:
        ballSpeedY = -ballSpeedY
    if ballRect.bottom > screenY:
        # Taaskäivitab palli kui on vastu seina läinud ja võtab punkti maha.
        ballRect.center = (screenX // 2, screenY // 2)
        ballSpeedX = 5
        ballSpeedY = 5
        score -= 1

    # Aluse liigutamine
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        paddleRect.x -= paddleSpeed
    if keys[pygame.K_d]:
        paddleRect.x += paddleSpeed

    # Kontrollib kas alus on vastu seina
    if paddleRect.left < 0:
        paddleRect.left = 0
    if paddleRect.right > screenX:
        paddleRect.right = screenX

    # Kontrollib kas pall on aluse vastu läinud
    if ballRect.colliderect(paddleRect) and ballSpeedY > 0:
        ballSpeedY = -ballSpeedY
        score += 1

    # Värskendab ekraani
    screen.fill((200, 200, 200))

    # Lisab palli ja aluse
    screen.blit(ballImg, ballRect)
    screen.blit(paddleImg, paddleRect)

    # Hooldab skoori
    scoreText = scoreFont.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(scoreText, (10, 10))

    # Hoiab ekraani töös
    pygame.display.flip()

# Väljub mängust
pygame.quit()