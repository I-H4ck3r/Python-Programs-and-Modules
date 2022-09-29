from tkinter import*

root = Tk()
root.minsize(300,300)
root.maxsize(500,500)

l1 = Label(root,text="Enter Username",font=("Arial",20))
l1.grid(row=0, column=0, pady=25)

e1 = Entry(root,font=("Arial",20))
e1.grid(row=0, column=1, pady=25)

l2 = Label(root,text="Enter Password",font=("Arial",20))
l2.grid(row=1, column=0, pady=25)

e2 = Entry(root,font=("Arial",20))
e2.grid(row=1, column=1, pady=25)

b1 = Button(root,text="Click!!",font=("Arial",20))
b1.grid(row=2, column=0, columnspan=2)

root.mainloop()
