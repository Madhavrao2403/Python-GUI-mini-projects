from tkinter import *
import time

root = Tk()
root.geometry("600x400")
root.title("Digital Clock")
root.configure(bg="black")

l1 = Label(root, font=("Arial", 100, "bold"), fg="white", bg="black")
l1.pack(expand=True, fill='both')

def clock_time():
    clock = time.strftime("%I:%M:%S %p")
    l1.config(text=clock)
    l1.after(200, clock_time)

clock_time()  # Start the clock update loop
root.mainloop()
