from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe By DK")

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

conditions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

player = "X"
stopgame = False

def execute(r, c):
    global player

    if player == "O" and conditions[r][c] == 0 and stopgame == False:
        a[r][c].configure(text="O", fg='orange', bg='black')
        conditions[r][c] = "O"
        player = "X"

    elif player == "X" and conditions[r][c] == 0 and stopgame == False:
        a[r][c].configure(text="X", fg='blue', bg='white')
        conditions[r][c] = "X"
        player = "O"

    else:
        messagebox.showinfo("Gadbad Ghotala!", "Galat Move H Be !")

    jeet()

def jeet():
    global stopgame

    for i in range(3):
        if conditions[i][0] == conditions[i][1] == conditions[i][2] != 0:
            a[i][0].config(bg='grey')
            a[i][1].config(bg='grey')
            a[i][2].config(bg='grey')
            stopgame = True

    for i in range(3):
        if conditions[0][i] == conditions[1][i] == conditions[2][i] != 0:
            a[0][i].config(bg='grey')
            a[1][i].config(bg='grey')
            a[2][i].config(bg='grey')
            stopgame = True

        if conditions[0][0] == conditions[1][1] == conditions[2][2] != 0:
            a[0][0].config(bg='grey')
            a[1][1].config(bg='grey')
            a[2][2].config(bg='grey')
            stopgame = True

        if conditions[2][0] == conditions[1][1] == conditions[0][2] != 0:
            a[2][0].config(bg='grey')
            a[1][1].config(bg='grey')
            a[0][2].config(bg='grey')
            stopgame = True

for q in range(3):
    for w in range(3):
        a[q][w] = Button(root, font=('Arial', 50), width=4, bg='snow', command=lambda r=q, c=w: execute(r, c))
        a[q][w].grid(row=q, column=w)

root.mainloop()
