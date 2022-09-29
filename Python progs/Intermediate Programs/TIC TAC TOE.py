from tkinter import*

root = Tk()
root.minsize(300,300)

c=1
def show (b):
    global c
    c = c+1
    if(c%2==0):
        if(b["text"]==""):
               b["text"] = "X"
    else:
        if(b["text"]==""):
               b["text"] = "0"
    if(b1["text"]=="0") and (b2["text"]=="0") and (b3["text"]=="0"):
        print("Player 0 is winner")
    if(b1["text"]=="X") and (b2["text"]=="X") and (b3["text"]=="X"):
        print("Player X is winner")
    if(b4["text"]=="0") and (b5["text"]=="0") and (b6["text"]=="0"):
        print("Player 0 is winner")
    if(b4["text"]=="X") and (b5["text"]=="X") and (b6["text"]=="X"):
        print("Player X is winner")
    if(b7["text"]=="0") and (b8["text"]=="0") and (b9["text"]=="0"):
        print("Player 0 is winner")
    if(b7["text"]=="X") and (b8["text"]=="X") and (b9["text"]=="X"):
        print("Player X is winner")
    if(b1["text"]=="0") and (b4["text"]=="0") and (b7["text"]=="0"):
        print("Player 0 is winner")
    if(b1["text"]=="X") and (b4["text"]=="X") and (b7["text"]=="X"):
        print("Player X is winner")
    if(b2["text"]=="0") and (b5["text"]=="0") and (b8["text"]=="0"):
        print("Player 0 is winner")
    if(b2["text"]=="X") and (b5["text"]=="X") and (b8["text"]=="X"):
        print("Player X is winner")
    if(b3["text"]=="0") and (b8["text"]=="0") and (b9["text"]=="0"):
        print("Player 0 is winner")
    if(b3["text"]=="X") and (b8["text"]=="X") and (b9["text"]=="X"):
        print("Player X is winner")
    if(b1["text"]=="0") and (b5["text"]=="0") and (b9["text"]=="0"):
        print("Player 0 is winner")
    if(b1["text"]=="X") and (b5["text"]=="X") and (b9["text"]=="X"):
        print("Player X is winner")
    if(b2["text"]=="0") and (b5["text"]=="0") and (b7["text"]=="0"):
        print("Player 0 is winner")
    if(b2["text"]=="X") and (b5["text"]=="X") and (b7["text"]=="X"):
        print("Player X is winner")

b1 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda: show(b1))
b1.grid(row=0,column=0)
b2 = Button(root,text="",font=("Arial",20),fg="purple",bg="orange",width="10",height="5",command= lambda: show(b2))
b2.grid(row=0,column=1)
b3 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda: show(b3))
b3.grid(row=0,column=2)

b4 = Button(root,text="",font=("Arial",20),fg="purple",bg="orange",width="10",height="5",command= lambda: show(b4))
b4.grid(row=1,column=0)
b5 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda: show(b5))
b5.grid(row=1,column=1)
b6 = Button(root,text="",font=("Arial",20),fg="purple",bg="orange",width="10",height="5",command= lambda: show(b6))
b6.grid(row=1,column=2)

b7 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda: show(b7))
b7.grid(row=2,column=0)
b8 = Button(root,text="",font=("Arial",20),fg="purple",bg="orange",width="10",height="5",command= lambda: show(b8))
b8.grid(row=2,column=1)
b9 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda: show(b9))
b9.grid(row=2,column=2)

root.mainloop()
