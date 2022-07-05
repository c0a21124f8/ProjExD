import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    beimg_sfc = pg.image.load("fig/pg_bg.jpg")  #Surface
    beimg_rct = beimg_sfc.get_rect()         #Rect
    screen_sfc.blit(beimg_sfc,beimg_rct)
    #pg.display.update()
    clock.tick(0.2)

    while True:
        screen_sfc.blit(beimg_sfc,beimg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()     #これから実装するゲームのメイン部分
    pg.quit()
    sys.exit()
