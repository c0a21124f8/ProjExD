import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key,tori
    key = event.keysym
    


def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    #if key == "":
    #    cx += 0
    #elif key == "Up":
    #    cy -= 20
    #elif key == "Down":
    #    cy += 20
    #elif key == "Left":
    #    cx -= 20
    #elif key == "Right":
    #    cx += 20

    delta = {"Up":[0,-1],"Down":[0,+1],"Left":[-1,0],"Right":[+1,0]}
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my,mx = my + delta[key][1], mx + delta[key][0]
    except:
        pass
    #if maze_bg[cx + mx * 100+50][cx + my*100+50] == 0:

    #if key == "Up": my -= 1
    #if key == "Down": my += 1
    #if key == "Left": mx -= 1
    #if key == "Right": mx += 1
    cx, cy = mx * 100+50, my*100+50
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    maze_bg = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg) # 1:壁/0:床を表す二次元リスト
    #print(maze_bg)

    tori = tk.PhotoImage(file= "fig/8.png")
    mx, my = 1, 1
    cx, cy = mx * 100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag = "tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()

