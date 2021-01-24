from tkinter import *
import tkinter.messagebox
tk= Tk()
tk.title("TIC TAC TOE")
playera = StringVar()
playerb = StringVar()
ptr1=0
ptr2=0
flag=True
ctr=1


def play(button):
    global flag,ctr
    if button["text"]==" " and flag==True:
        flag=False
        button["text"]="X"
        ctr+=1
        Check()
    elif button["text"]==" " and flag==False:
        flag=True
        button["text"]="O"
        ctr+=1
        Check()
    else:
        tkinter.messagebox.showinfo("TIC TAC TOE", "Button already Clicked!")
def ClearButton():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
def Check():
    global ptr1,ptr2,playera,playerb,ctr
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        ClearButton()
        tkinter.messagebox.showinfo("TIC TAC TOE", "player 1 win")
        ptr1=+1
        ctr=0
        playera.set(ptr1)
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'   or
        button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'   or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'   or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'   or
        button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'   or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'   or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'   or
        button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        ClearButton()
        tkinter.messagebox.showinfo("TIC TAC TOE", "player 2 win")
        ptr2=+1
        ctr=0
        playerb.set(ptr2)
    elif (ctr==8):
        tkinter.messagebox.showinfo("TIC TAC TOE", "It is a Tie game")
button1 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button1))
button1.grid(row=1, column=0)
button2 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button2))
button2.grid(row=1, column=1)
button3 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button3))
button3.grid(row=1, column=2)
button4 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button4))
button4.grid(row=2, column=0)
button5 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button5))
button5.grid(row=2, column=1)
button6 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button6))
button6.grid(row=2, column=2)
button7 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button7))
button7.grid(row=3, column=0)
button8 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button8))
button8.grid(row=3, column=1)
button9 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='black', height=1, width=8,
                 command=lambda: play(button9))
button9.grid(row=3, column=2)

label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=4, column=0,columnspan=2)
p1=Entry(tk, textvariable=playera,bd=5,width=6)
p1.grid(row=4,column=2)


label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=5, column=0,columnspan=2)
p2=Entry(tk, textvariable=playerb,bd=5,width=6)
p2.grid(row=5,column=2)
tk.mainloop()
