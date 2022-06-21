import tkinter as tk
import tkinter.messagebox as tkm
import math

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")

    def button_click(event):
        btn = event.widget
        txt = btn["text"]
        #tkm.showinfo(txt,f"[{txt}]ボタンがクリックされました")
        if txt == "=":
            ans = entry.get()
            ans01 = eval(ans)
            entry.delete(0,tk.END)
            entry.insert(tk.END, ans01)
        elif txt == "sin":
            ans = entry.get()
            ans.replace(txt,"")
            entry.delete(0,tk.END)
            ans01 = math.sin(int(ans))
            entry.insert(tk.END, ans01)
        elif txt == "cos":
            ans = entry.get()
            ans.replace(txt,"")
            entry.delete(0,tk.END)
            ans01 = math.cos(int(ans))
            entry.insert(tk.END, ans01)
        elif txt == "tan":
            ans = entry.get()
            ans.replace(txt,"")
            entry.delete(0,tk.END)
            ans01 = math.tan(int(ans))
            entry.insert(tk.END, ans01)
        elif txt == "π":
            ans = entry.get()
            ans.replace(txt,"")
            entry.delete(0,tk.END)
            ans01 = int(ans)*3.141592653
            entry.insert(tk.END, ans01)
        else:
            entry.insert(tk.END, txt)
        


    entry = tk.Entry(root,justify = "right",width = 15,font = ("Times New Roman",40))
    entry.grid(row = 0,column = 0,columnspan = 4)

    
    word_box = ["π","sin","cos","tan"]
    m = 1
    for i in range(1,5):        #列指定(テキスト入力欄があるので１段下げる)
        for j in range(0,4):    #行指定
            if i == 4 and j == 1 :    #＋ボタンの位置になったとき実行
                a = "+"
            elif i == 4 and j == 2:    #＝ボタンの位置になったとき実行
                a = "="
            elif i == m and j == 3:
                a = word_box[m-1]
                m += 1
            else:
                a = 9 - (3 * (i-1)) - j     #数字計算
            button = tk.Button(root,text = f"{a}",width = 4, height=2,font = ("Times New Roman", 30))
            button.grid(row = i,column = j)
            button.bind("<1>", button_click)
    

    root.mainloop()




