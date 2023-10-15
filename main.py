import pygame
import math

# Dimensions of screen
DIMENSIONS = [1400, 800]

# X values list
x_vals = []

# Range of x values
for i in range(-400, 800):
    x_vals.append(i)

# Points of the equations
points = []

# Scale of Graph, can be controlled with arrow keys UP and DOWN
size = 10

# Offset of the graph, can be controlled with awsd
offset = [0, 0]

pygame.init()
pygame.display.set_caption('Graph')
screen = pygame.display.set_mode(DIMENSIONS)
clock = pygame.time.Clock()

#Event Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cx, cy = pygame.mouse.get_pos()

        mx, my = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        size += 1
        points.clear()
    if keys[pygame.K_DOWN]:
        if size > 1:
            size -= 1
            points.clear()
    if keys[pygame.K_a]:
        offset[0] += 15
        points.clear()
    if keys[pygame.K_d]:
        offset[0] -= 15
        points.clear()
    if keys[pygame.K_w]:
        offset[1] += 15
        points.clear()
    if keys[pygame.K_s]:
        offset[1] -= 15
        points.clear()

    #Background
    screen.fill((30, 30, 30))

    #Fonts
    font = pygame.font.SysFont("twcencondensedextra", 60)
    font_small = pygame.font.SysFont("twcencondensedextra", 20)

    # Graph Lines
    pygame.draw.line(screen, (255, 255, 255), (0 + offset[0], DIMENSIONS[1]/2 + offset[1]), (DIMENSIONS[0] + offset[0], DIMENSIONS[1]/2 + offset[1]))
    pygame.draw.line(screen, (255, 255, 255), (DIMENSIONS[0]/2 + offset[0], 0), (DIMENSIONS[0]/2 + offset[0], DIMENSIONS[1] + offset[1]))

    for x in x_vals:
        y = x**2
        # Example Equations
        # y = x**3
        # y = abs(x)
        # y = math.sqrt(x)
        points.append((x*size + DIMENSIONS[0]/2 - 2, DIMENSIONS[1]/2 - y*size - 2))
    for point in points:
        if points.index(point) < len(points) - 1:
            if points.index(point) < 850:
                pygame.draw.line(screen, (255, 255, 255), (point[0] + 1 + offset[0], point[1] + 1+ offset[1]), (points[points.index(point) + 1][0] + 1 + offset[0], points[points.index(point) + 1][1] + 1 + offset[1]), 4)

    pygame.display.update()
    clock.tick(120)