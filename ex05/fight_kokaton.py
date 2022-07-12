import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)    # Surface
        self.rct = self.sfc.get_rect()        # Rect
        self.bgi_sfc = pg.image.load(image)   # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()              # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen): #矢印キー操作モード
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)
    
    def mouse_move(self, r, scr:Screen): #マウス操作モード(rはマウスの座標)
        self.rct.center = r      #こうかとんの座標を更新する
        self.blit(scr)           #更新

    def attack(self):
        return Shot(self)


class Shot:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/beams_long.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.05)
        self.rct = self.sfc.get_rect()
        self.rct.center = chr.rct.midright

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.rct.move_ip(+10, 0) #右方向に速度１で移動する
        self.blit(scr)
        if check_bound(self.rct, scr.rct) != (1,1): #領域外に出たら、インスタンスを消す
            del self
        

class Bomb():
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((size * 2, size * 2)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Score(self,score):
    def __init__(self):
        self.font = pg.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = (255, 0, 0)
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if self.score != self.lastscore:
            self.lastscore = self.score
            msg = "Score: %d" 
            self.image = self.font.render(msg, 0, self.color)

def main():
    score = 0 #スコアの初期値
    a = 6     #こうかとんの画像の番号の初期値
    mode = 1  #矢印キーそうさとマウス操作を入れ替える変数（初期値は矢印キー操作）
    clock = pg.time.Clock()
    scr = Screen("逃げろ！ファミチキ！", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird(f"fig/{a}.png", 2.0, (900, 400))
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    beams = None

    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:   #クリックするとスキンを変更する
                x, y = kkt.rct.center                         #現在地を格納する
                a = (a + 1) % 11                              #1-10の画像番号を順に表示する
                kkt = Bird(f"fig/{a}.png", 2.0, (x, y))       #番号に対応した画像をこうかとんの位置で更新する
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_2:  
                    mode = 2             #２のキーをクリックするとマウス移動モードに変更
                if event.key == pg.K_1:  
                    mode = 1             #１のキーをクリックすると十字キー移動モードに変更
                if event.key == pg.K_SPACE:
                    beams = kkt.attack() #スペースキーが押されたらこうかとんがBEAMSを撃つ
                    
        if mode == 1:
            kkt.update(scr)
        if mode == 2:
            r = pg.mouse.get_pos()  #マウスの座標を格納
            kkt = Bird(f"fig/{a}.png", 2.0, r)   #こうかとんの位置を格納した座標に変更する
            kkt.mouse_move(r, scr)
        
        bkd.update(scr)

        if beams:
            beams.update(scr)
            if beams.rct.colliderect(bkd.rct):
                tkm.showinfo("おめでとう！", "ゲームクリア！") #ビームが出ている時に的に命中するとゲームクリアのテロップを表示する
                return    #テロップを表示した後ゲームを終了する
        
        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 # 領域内

    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()