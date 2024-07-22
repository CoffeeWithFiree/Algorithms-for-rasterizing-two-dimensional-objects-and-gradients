import pygame as pg
from Rasterization2D import Rasterization2D

pg.init()

#The viewing window has a size of Vw by Vh

Vw, Vh = 800, 600

screen = pg.display.set_mode((Vw, Vh))
pg.display.set_caption('Rasterization')

graphic = Rasterization2D(screen)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # graphic.DrawLineBresenhamV4([200, 200], [200, 300], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([100, 100], [300, 200], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([100, 200], [300, 100], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([200, 300], [400, 500], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([400, 300], [200, 200], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([350, -100], [460, 340], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([90, 90], [300, 90], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([220, 220], [400, 500], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([200, 100], [000, 000], (83, 55, 122))
    # graphic.DrawLineBresenhamV4([100, 100], [200, 300], (83, 55, 122))


    # graphic.DrawTriangle([100, 100], [300, 200], [300, 90], (83, 55, 122))
    # graphic.DrawFilledTriangle([100, 100], [100, 300], [300, 100], (83, 55, 122))
    # graphic.DrawFilledTriangle([300, 300], [500, 400], [500, 290], (83, 55, 122))
    # graphic.DrawFilledTriangle([100, 100], [100, 300], [300, 100], (83, 55, 122))
    #
    # graphic.DrawTriangle([300, 300], [500, 400], [500, 290], (0, 0, 0))
    # graphic.DrawTriangle([100, 100], [100, 300], [300, 100], (0, 0, 0))

    # graphic.DrawShadedTriangle([300, 300, 0.5], [500, 400, 0.9], [500, 290, 0], (83, 55, 122))
    # graphic.DrawShadedTriangle([100, 100, 0.9], [100, 300, 0.1], [300, 100, 0.5], (83, 55, 122))

    color0 = [255, 0, 0]
    color1 = [0, 255, 0]
    color2 = [0, 0, 255]

    P0 = [100, 100]
    P1 = [300, 200]
    P2 = [300, 90]

    graphic.DrawGradientTriangle(P0, P1, P2, color0, color1, color2)
    graphic.DrawGradientTriangle([300, 400], [500, 500], [500, 390], [82, 122, 55], [10, 58, 0], [0, 55, 100])
    graphic.DrawGradientTriangle([400, 100], [400, 300], [600, 100], [83, 55, 122], [255, 34, 100], [65, 0, 65])

    # graphic.DrawFilledTriangle([100, 100], [300, 200], [300, 90], (83, 55, 122))
    # graphic.DrawTriangle([100, 100], [300, 200], [300, 90], (0, 0, 0))

    pg.display.flip()

pg.quit()