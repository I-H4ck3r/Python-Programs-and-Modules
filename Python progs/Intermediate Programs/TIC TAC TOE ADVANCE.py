from tkinter import*
import tkinter.messagebox
root = Tk()
root.title("Tic Tac Toe")

click = True

def show (b):
    global click
    if b["text"] == "" and click == True:
        b["text"] = "X"
        click = False
    elif b["text"] == "" and click == False:
        b["text"] = "O"
        click = True
        
    elif (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or
        b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or
        b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or
        b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or
        b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or
        b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" or
        b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or
        b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        tkinter .messagebox.showinfo("Winner X", "You have just won a game")

    elif (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or
        b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or
        b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" or
        b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or
        b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or
        b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" or
        b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or
        b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        tkinter .messagebox.showinfo("Winner O", "You have just won a game")
                                                         
b1 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda:show(b1))
b1.grid(row=0,column=0,sticky= N+S+W+E)
b2 = Button(root,text="",font=("Arial",20),fg="purple",bg="orange",width="10",height="5",command= lambda:show(b2))
b2.grid(row=0,column=1,sticky= N+S+W+E)
b3 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda:show(b3))
b3.grid(row=0,column=2,sticky= N+S+W+E)

b4 = Button(root,text="",font=("Arial",20),fg="purple",bg="orange",width="10",height="5",command= lambda:show(b4))
b4.grid(row=1,column=0,sticky= N+S+W+E)
b5 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda:show(b5))
b5.grid(row=1,column=1,sticky= N+S+W+E)
b6 = Button(root,text="",font=("Arial",20),fg="purple",bg="orange",width="10",height="5",command= lambda:show(b6))
b6.grid(row=1,column=2,sticky= N+S+W+E)

b7 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda:show(b7))
b7.grid(row=2,column=0,sticky= N+S+W+E)
b8 = Button(root,text="",font=("Arial",20),fg="purple",bg="orange",width="10",height="5",command= lambda:show(b8))
b8.grid(row=2,column=1,sticky= N+S+W+E)
b9 = Button(root,text="",font=("Arial",20),fg="red",bg="cyan",width="10",height="5",command= lambda:show(b9))
b9.grid(row=2,column=2,sticky= N+S+W+E) 

root.mainloop()
