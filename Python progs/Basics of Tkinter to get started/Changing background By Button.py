from tkinter import*

root = Tk()
root.minsize(300,300)
root.maxsize(500,500)

def show():
    root.configure(background="cyan")

b1 = Button(root,text="Click!!",font=("Arial",20))
b1.config(command=show)
b1.pack()

root.mainloop()
