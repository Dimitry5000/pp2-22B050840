import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
running = True
radius = 25
x = 250
y = 250
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - radius - 20 >= 0:
            y -= 20
        if pressed[pygame.K_DOWN] and y + radius + 20 <= 500:
            y += 20
        if pressed[pygame.K_LEFT] and x - radius - 20 >= 0:
            x -= 20
        if pressed[pygame.K_RIGHT] and x + radius + 20 <= 500:
            x += 20
        screen.fill((0,0,0))
        pygame.draw.circle(color=(255,0,0) ,surface=screen , center=(x,y), radius=radius) 
    pygame.display.flip()