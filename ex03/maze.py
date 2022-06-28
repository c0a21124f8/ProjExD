import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "":
        cx += 0
    elif key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    elif key == "":
        cx += 0
    canvas.coords("tori",cx,cy)
    root.after(50,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    key = ""
    tori = tk.PhotoImage(file= "fig/8.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag = "tori")
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()

