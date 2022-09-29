from tkinter import*

root = Tk()
root.minsize(300,300)
root.maxsize(500,500)

l1 = Label(root,text="Divyansh\nAgrawal",font=("Arial",20),fg="red",bg="yellow",width="10",height="2")
l1.pack()

e1 = Entry(root,font=("Arial",20),fg="pink",bg="green",width="10")
e1.pack()

b1 = Button(root,text="Click!!",font=("Arial",20),fg="orange",bg="cyan",width="10",height="2")
b1.pack()

root.mainloop()
