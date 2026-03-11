import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    # add the object to the blanc screen with RGB and positioning
    # x = 100   → 100 pixels from the left
    # y = 100   → 100 pixels from the top
    # width = 20
    # height = 20
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 20, 20))
    pygame.display.update()

pygame.quit()
