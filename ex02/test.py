
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("おかめしか")
root.geometry("500x200")

lavel = tk.Label(root,
                text = "100万回押すとオーブ100万個もらえるよ！",
                font = ("Ricty Diminished", 20)
                )
lavel.pack()

button = tk.Button(root,text = "タップ！！！", command =button_click)
button.bind("<1>", button_click)
button.pack()

entry = tk.Entry(width = 30)
entry.insert(tk.END, "モンスト　オーブ　無料配布")
entry.pack()



root.mainloop()