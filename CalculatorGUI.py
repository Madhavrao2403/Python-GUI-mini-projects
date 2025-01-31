from tkinter import *

root = Tk()
root.geometry("1920x1080")
root.title("Calculator")
root.iconphoto(False, PhotoImage(file=r"src\logo.png"))
root.configure(bg="#1E1E1E")

display = Entry(root, font=("Arial", 40), fg="white", bg="#1E1E1E", bd=0, justify="right", insertbackground="white")
display.insert(0, "0")
display.place(x=40, y=30, width=1151, height=80)

def button_pressed(event):
    text = event.widget.cget("text")
    current_text = display.get()
    if text=="x":
        text="*"
    if current_text == "0":
        display.delete(0, END)
    if text == "=":
        try:
            result = eval(current_text)
            display.delete(0, END)
            display.insert(0, str(result))
        except  ZeroDivisionError:
            display.delete(0,END)
            display.insert(0,"Invalid")    
    elif text=="AC":
        display.delete(0,END)   
        display.insert(0,"0") 
    elif text=="delete":
        display.delete(len(current_text)-1)      
        if not display.get():
            display.insert(0,"0")
    else:
        display.insert(END, text)

def button(text, x, y):
    width = 15
    height = 2
    bg = "#333333"
    fg = "white"
    if text == "0":
        width = 36
    if text in ["/", "%", "x", "-", "+", "="]:
        bg = "yellow"
        fg = "black"
    btn = Button(root, text=text, width=width, height=height, font=("Arial", 18, "bold"), justify="center", bg=bg, fg=fg, bd=0)
    btn.place(x=x, y=y)
    btn.bind("<Button-1>", button_pressed)

buttons1 = ["AC", "7", "4", "1", "0"]
for i, btn_text in enumerate(buttons1):
    button(btn_text, 40, 130 + i * 100)

buttons2 = ["/", "8", "5", "2"]
for i, t in enumerate(buttons2):
    button(t, 350, 130 + i * 100)

buttons3 = ["%", "9", "6", "3", "."]
for i, t in enumerate(buttons3):
    button(t, 660, 130 + i * 100)

buttons4 = ["x", "-", "+", "=","delete"]
for i, t in enumerate(buttons4):
    button(t, 970, 130 + i * 100)

root.mainloop()
