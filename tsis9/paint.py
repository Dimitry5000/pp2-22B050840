import pygame
import math
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    shape = "rect"
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    points = []
                    screen.fill((0,0,0))
                elif event.key == pygame.K_c:
                    shape = "circle"
                elif event.key == pygame.K_p:
                    shape = "rect"
                elif event.key == pygame.K_l:
                    shape = "line"
                elif event.key == pygame.K_s:
                    shape = "square"
                elif event.key == pygame.K_1:
                    shape = "rtr"
                elif event.key == pygame.K_2:
                    shape = "etr"
                elif event.key == pygame.K_3:
                    shape = "rh"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            if shape == "line": #default mode
                if event.type == pygame.MOUSEMOTION:
                    # if mouse moved, add point to list
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                
                screen.fill((0, 0, 0))
        
                # draw all points
                i = 0
                while i < len(points) - 1:
                    drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                    i += 1
            if shape == "rh": #draw rhombus if pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    pygame.draw.polygon(screen, mode, ([position[0], position[1]], [position[0] - radius, position[1] + radius], [position[0], position[1] + 2 * radius], [position[0] + radius, position[1] + radius]))
            if shape == "rtr": #draw right triangle if pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    pygame.draw.polygon(screen, mode, ([position[0], position[1]], [position[0], position[1] + radius], [position[0] + radius, position[1] + radius]))
            if shape == "etr": #draw equilateral triangle if pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    half = radius / math.tan(math.pi/3)
                    pygame.draw.polygon(screen, mode, ([position[0], position[1]], [position[0] - half, position[1] + radius], [position[0] + half, position[1] + radius]))
            if shape == "square": #draw square if pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    pygame.draw.rect(
                        screen,
                        mode,
                        pygame.Rect(
                        position[0] - radius,
                        position[1] - radius,
                        2 * radius,
                        2 * radius
                        )
                    )
            if shape == "circle": #draw circle if pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pygame.draw.circle(screen, mode, event.pos, radius)
            if shape == "rect": #draw rectangle if pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    startposition = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    endposition = event.pos
                    startposx = min(startposition[0], endposition[0])
                    startposy = min(startposition[1], endposition[1])
                    endposx = max(startposition[0], endposition[0])
                    endposy = max(startposition[1], endposition[1])
                    pygame.draw.rect(screen, mode, pygame.Rect(
                        startposx,
                        startposy,
                        endposx - startposx,
                        endposy - startposy
                            ))
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()