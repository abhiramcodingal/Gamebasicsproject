import pygame

pygame.init()
surface1 = pygame.display.set_mode((640,480))
pygame.display.set_caption("My first game screen")

done = False
rectangle = pygame.Rect(640/2-30, 480/2-30, 90, 70)
d_green = (12, 66, 9)
d_blue = (9, 18, 66)
txt = pygame.font.Font(None, 30).render("Rectangle" ,True, d_blue)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    surface1.fill((255,255,255))
    pygame.draw.rect(surface1, d_green, rectangle)
    surface1.blit(txt, (640/2-35,480/2-50))
    pygame.display.flip()

pygame.quit()   