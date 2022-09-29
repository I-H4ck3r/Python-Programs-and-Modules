from tkinter import*

root = Tk()
root.minsize(300,300)
root.maxsize(500,500)

def show():
    print("Divyansh Agrawal")

b1 = Button(root,text="Click!!",font=("Arial",20),command=show)
b1.pack()

root.mainloop()
