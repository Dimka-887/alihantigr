import pygame
pygame.init()
dis=pygame.display.set_mode((600,400))
# r = pygame.Rect(50,50,150,100)
dis.fill(((55,5,55)))
while not dis_over:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    pygame.draw.circle(dis, [250, 250, 250], [300, 300], 60)
    pygame.draw.circle(dis, [250, 250, 250], [300, 200], 45)
    pygame.draw.circle(dis, [250, 250, 250], [300, 120], 30)
    pygame.draw.circle(dis, [0, 0, 0], [290, 115], 5)
    pygame.draw.circle(dis, [0, 0, 0], [310, 115], 5)
    pygame.draw.polygon(dis, [250, 165, 0], [(300, 125),(300,135),(330,130)])
    pygame.draw.circle(dis, [0, 0, 0], [300, 180], 5)
    pygame.draw.circle(dis, [0, 0, 0], [300, 200], 5)
    pygame.draw.circle(dis, [0, 0, 0], [300, 220], 5)
    pygame.draw.line(dis, [80, 50, 20], [260, 200], (190,180), 4)
    pygame.draw.line(dis, [80, 50, 20], (340, 210), (410,180),  4)
    pygame.draw.polygon(dis, (0, 0, 0), [(260, 110), (340, 110), (320,70), (280,70)])
    pygame.display.update()

