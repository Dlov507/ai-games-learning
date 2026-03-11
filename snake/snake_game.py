import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

running = True
# velocity variables
x = 100
y = 100
dx = 0
dy = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                dx = 5
                dy = 0
            if event.type == pygame.K_LEFT:
                dx = -5
                dy = 0
            if event.type == pygame.K_UP:
                dx = 0
                dy = -5
            if event.type == pygame.K_DOWN:
                dx = 0
                dy = 5
    x += dx
    y += dy

    screen.fill((0, 0, 0))
    # add the object to the blanc screen with RGB and positioning
    # x = 100   → 100 pixels from the left
    # y = 100   → 100 pixels from the top
    # width = 20
    # height = 20
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 20, 20))
    pygame.display.update()

pygame.quit()
