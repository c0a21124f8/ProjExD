import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    root.geometry("300x600")

    def button_click(event):
        btn = event.widget
        txt = btn["text"]
        #tkm.showinfo(txt,f"[{txt}]ボタンがクリックされました")
        entry.insert(tk.END, txt)

    entry = tk.Entry(root,justify = "right",width = 10,font = ("Times New Roman",40))
    entry.grid(row = 0,column = 0,columnspan = 3)


    for i in range(1,5):
        for j in range(0,3):
            if (i == 4 and j == 1) :
                button = tk.Button(root,text = "+",width = 4, height=2,font = ("Times New Roman", 30))
                button.grid(row = i,column = j)
                button.bind("<1>", button_click)
            elif(i == 4 and j == 2):
                button = tk.Button(root,text = "=",width = 4, height=2,font = ("Times New Roman", 30))
                button.grid(row = i,column = j)
                button.bind("<1>", button_click)
            else:
                a = 9 - (3 * (i-1)) - j
                button = tk.Button(root,text = f"{a}",width = 4, height=2,font = ("Times New Roman", 30))
                button.grid(row = i,column = j)
                button.bind("<1>", button_click)
    

    root.mainloop()




