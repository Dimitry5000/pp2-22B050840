import pygame
pygame.init()
screen = pygame.display.set_mode((1200,500))
running = True
image = pygame.image.load("mickeyclock.jpeg")
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0,0,0))
        angle = 20
        rotatedimage = pygame.transform.rotate(image, angle)
        screen.blit(rotatedimage, (0,0))
        clock.tick(60)
    pygame.display.flip()