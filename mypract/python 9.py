#from turtle import color
import pygame


pygame.init()
screen = pygame.display.set_mode((600,600))
color = (173,223,173)
font = pygame.font.SysFont(None,30)
text_surface = font.render("1", True, color)
running = True
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        pygame.quit()
    for x in range(10,600,50):
        for y in range(1,600,50):
            pygame.draw.rect(screen,color,(x, y, 40,40),1)
    pygame.display.update()
quit()

