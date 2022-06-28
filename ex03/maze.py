import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def change_chicken(event):  #画像フォルダにある画像を入れ替える関数
    global tori,cx,cy,a,i
    i = (i + 1) % 11        #画像番号をクリックするごとに＋１して画像を入れ替える
    a = f"fig/{i}.png"
    

def main_proc():
    global cx, cy, mx, my,a,tori,i
    delta = {"Up":[0,-1],"Down":[0,+1],"Left":[-1,0],"Right":[+1,0]}
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my,mx = my + delta[key][1], mx + delta[key][0]
    except:
        pass

    cx, cy = mx * 100+50, my*100+50
    tori = tk.PhotoImage(file= a)
    canvas.create_image(cx, cy, image=tori, tag = "tori")
    canvas.coords("tori",cx,cy)
    
    root.after(100,main_proc)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    maze_bg = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg) # 1:壁/0:床を表す二次元リスト

    a = "fig/8.png"
    tori = tk.PhotoImage(file= a)
    i = 8
    mx, my = 1, 1
    cx, cy = mx * 100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag = "tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.bind("<1>",change_chicken)
    main_proc()
    root.mainloop()

