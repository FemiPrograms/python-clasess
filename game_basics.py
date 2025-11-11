'''import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()'''

import pygame
pygame.init()
display_surface = pygame.display.set_mode((500,500))
pygame.display.set_caption('Adding image and backgraound image')
background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (500,500))

penguin_image = pygame.transform.scale(
    pygame.image.load('penguin.png').convert_alpha(), (200,200))
penguin_rect = penguin_image.get_rect(center=(500//2,
                                              500// 2 - 30))
text = pygame.font.Font(None, 36).render('Hello World', True,
                                        pygame.Color('black'))
text_rect = text.get_rect(center=(500 // 2, 500 // 2 + 110))