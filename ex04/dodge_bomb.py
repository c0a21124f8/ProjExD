import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    beimg_sfc = pg.image.load("fig/pg_bg.jpg")  #Surface
    beimg_rct = beimg_sfc.get_rect()         #Rect
    screen_sfc.blit(beimg_sfc,beimg_rct)

    #焼き鳥
    kkimg_sfc = pg.image.load("fig/20.png")     #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rct = kkimg_sfc.get_rect()            #Rect
    kkimg_rct.center = 900,400

    #爆弾
    bmimg_sfc = pg.Surface((20,20))   #Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10,10), 10)
    bmimg_rct = bmimg_sfc.get_rect()  #Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)

    while True:
        screen_sfc.blit(beimg_sfc,beimg_rct)
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True:   #ｙ座標を-1
            kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True: #ｙ座標を+1
            kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True: #ｘ座標を-1
            kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True:#ｘ座標を+1
            kkimg_rct.centerx += 1

        screen_sfc.blit(bmimg_sfc,bmimg_rct)

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()     #これから実装するゲームのメイン部分
    pg.quit()
    sys.exit()
