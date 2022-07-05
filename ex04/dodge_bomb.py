import pygame as pg
import sys
import random

def main():
    global a, mode
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    beimg_sfc = pg.image.load("fig/pg_bg.jpg")  #Surface
    beimg_rct = beimg_sfc.get_rect()         #Rect
    screen_sfc.blit(beimg_sfc,beimg_rct)

    #焼き鳥
    kkimg_sfc = pg.image.load(f"fig/{a}.png")     #Surface
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
    vx, vy = +1, +1

    while True:
        screen_sfc.blit(beimg_sfc,beimg_rct)
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:   #クリックするとスキンを変更する
                x, y = kkimg_rct.centerx, kkimg_rct.centery   #現在地を格納する
                a = (a + 1) % 11                              #1-10の番号を順に表示する
                kkimg_sfc = pg.image.load(f"fig/{a}.png")     #画像表示
                kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
                kkimg_rct = kkimg_sfc.get_rect()
                kkimg_rct.center = x, y                       #先程格納した座標を登録
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_2:  #２のキーをクリックすると
                    mode = 2             #マウス移動モードに変更
                if event.key == pg.K_1:  #１のキーをクリックすると
                    mode = 1             #十字キー移動モードに変更
            if event.type == pg.QUIT:
                return
        
        if mode == 2:               #マウス移動モード
            r = pg.mouse.get_pos()  #マウスの座標を格納
            kkimg_rct.center = r    #こうかとんの位置を格納した座標に変更する
        if mode == 1:               #十字キー移動モード
            key_states = pg.key.get_pressed()
            if key_states[pg.K_UP] == True:   #ｙ座標を-1
                kkimg_rct.centery -= 1
            if key_states[pg.K_DOWN] == True: #ｙ座標を+1
                kkimg_rct.centery += 1
            if key_states[pg.K_LEFT] == True: #ｘ座標を-1
                kkimg_rct.centerx -= 1
            if key_states[pg.K_RIGHT] == True:#ｘ座標を+1
                kkimg_rct.centerx += 1
            if check_bound(kkimg_rct, beimg_rct) != (1, 1):
                if key_states[pg.K_UP] == True:   #ｙ座標を-1
                    kkimg_rct.centery += 1
                if key_states[pg.K_DOWN] == True: #ｙ座標を+1
                    kkimg_rct.centery -= 1
                if key_states[pg.K_LEFT] == True: #ｘ座標を-1
                    kkimg_rct.centerx += 1
                if key_states[pg.K_RIGHT] == True:#ｘ座標を+1
                    kkimg_rct.centerx -= 1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        
        bmimg_rct.move_ip(vx, vy)

        screen_sfc.blit(bmimg_sfc,bmimg_rct)
        yoko, tate = check_bound(bmimg_rct, beimg_rct)
        vx *= yoko
        vy *= tate

        if kkimg_rct.colliderect(bmimg_rct):
            return

        pg.display.update()
        clock.tick(1000)
    
def check_bound(rct,scr_rct):
    #[１]　rct:　こうかとん　or　爆弾のRect
    #[２]　scr_rct:　スクリーンのRect
    yoko,  tate = +1, +1   #領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        yoko = -1          #領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = -1          #領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    mode = 1   #十字キー移動モード
    a = 2      #こうかとんの初期スキン
    main()     #これから実装するゲームのメイン部分
    pg.quit()
    sys.exit()
