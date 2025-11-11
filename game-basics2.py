import pygame

pygame.init()
'''screen = pygame.display.set_mode((400,300))
done = False
green = (0,255,0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0,125,255), pygame.Rect(30,30,60,60)) #pygame.draw.rect(surface, color, Rect(left, top, width, height), width)
    pygame.draw.circle(screen, green, (100,100), 50) #pygame.draw.circle(surface, color, center, radius, width)
    pygame.display.flip()'''
sw, sh = 500,500
screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption('color changing sprite')
colors = {
    'red' : pygame.Color('red'),
    'green' : pygame.Color('green'),
    'blue' : pygame.Color('blue'),
    'yellow' : pygame.Color('yellow'),
    'white' : pygame.Color('white')

    }
current_color = colors['white']

x, y = 30,30
spw, sph = 60, 60

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.key_pressed()
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3

    x = min(max(0, x), sw - spw)
    y = min(max(0, y), sh - sph)

    
