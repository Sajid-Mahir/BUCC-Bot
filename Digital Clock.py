from tkinter import* 
from tkinter.ttk import* 
from time import strftime

root=Tk()
root.title("Digital Clock")

def tick():
    s=strftime('%H:%M:%S %p')
    label.config(text=s)
    label.after(1000, tick)
label=Label(root,font=("ds-digital",200), background="blue", foreground="yellow")
label.pack(anchor='center')
tick()
mainloop()