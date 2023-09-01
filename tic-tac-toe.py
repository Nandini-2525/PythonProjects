from tkinter import *
from tkinter import messagebox

base = Tk()
print("Hello, I am Nandini")
base.geometry("360x380")
base.title("Tic-Tac-Toe")
ft1 = ("Halvetica", 20)


# X start so true
clicked = True
count = 0

# disable all the buttons
def disable_all_buttons():

    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)

    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)

    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)


# check if someone won
def checkifwon():
    global winner
    winner = False
    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
        btn1.config(bg="red")
        btn2.config(bg="red")
        btn3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! X wins...!")
        disable_all_buttons()

    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        btn4.config(bg="red")
        btn5.config(bg="red")
        btn6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! X wins...!")
        disable_all_buttons()

    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        btn7.config(bg="red")
        btn8.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! X wins...!")
        disable_all_buttons()

    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        btn1.config(bg="red")
        btn5.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! X wins...!")
        disable_all_buttons()

    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        btn3.config(bg="red")
        btn5.config(bg="red")
        btn7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! X wins...!")
        disable_all_buttons()

    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        btn1.config(bg="red")
        btn4.config(bg="red")
        btn7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! X wins...!")
        disable_all_buttons()

    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
        btn2.config(bg="red")
        btn5.config(bg="red")
        btn8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! X wins...!")
        disable_all_buttons()

    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        btn3.config(bg="red")
        btn6.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! X wins...!")
        disable_all_buttons()

 ##### CHECK FOR O's WINNER #####

    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        btn1.config(bg="red")
        btn2.config(bg="red")
        btn3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! O wins...!")
        disable_all_buttons()

    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        btn4.config(bg="red")
        btn5.config(bg="red")
        btn6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! O wins...!")
        disable_all_buttons()

    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        btn7.config(bg="red")
        btn8.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! O wins...!")
        disable_all_buttons()

    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        btn1.config(bg="red")
        btn5.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! O wins...!")
        disable_all_buttons()

    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        btn3.config(bg="red")
        btn5.config(bg="red")
        btn7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! O wins...!")
        disable_all_buttons()

    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        btn1.config(bg="red")
        btn4.config(bg="red")
        btn7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! O wins...!")
        disable_all_buttons()

    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
        btn2.config(bg="red")
        btn5.config(bg="red")
        btn8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! O wins...!")
        disable_all_buttons()

    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        btn3.config(bg="red")
        btn6.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATUATIONS! O wins...!")
        disable_all_buttons()

    # check if tie
    if count ==9 and winner == False:
        messagebox.showinfo("Tic tac Toe", "Its a Tie..! \n No one wins !")
        disable_all_buttons()


# button clicked function
def b_click(btn):
    global clicked, count

    if btn["text"] == " " and clicked == True:
        btn["text"] = "X"
        clicked = False
        count += 1
        checkifwon()

    elif btn["text"] == " " and clicked == False:
        btn["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("tic tac toe", "hey this box has been selected\n please pick another box")

def reset():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global clicked, count
    clicked = True
    count=0

    # buttons
    btn1 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn1), fg="black", width=6, height=3)
    btn2 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn2), fg="black", width=6, height=3)
    btn3 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn3), fg="black", width=6, height=3)

    btn4 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn4), fg="black", width=6, height=3)
    btn5 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn5), fg="black", width=6, height=3)
    btn6 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn6), fg="black", width=6, height=3)

    btn7 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn7), fg="black", width=6, height=3)
    btn8 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn8), fg="black", width=6, height=3)
    btn9 = Button(base, text=" ", font=ft1, bg="SystemButtonFace", command= lambda : b_click(btn9), fg="black", width=6, height=3)

    # grid buttons
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)

    btn4.grid(row=1, column=0)
    btn5.grid(row=1, column=1)
    btn6.grid(row=1, column=2)

    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)

# create menu
my_menu = Menu(base)
base.config(menu=my_menu)

# create option menu
options_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "Options", menu=options_menu)
options_menu.add_command(label="Reset Game",command=reset)

reset()

base.mainloop()
