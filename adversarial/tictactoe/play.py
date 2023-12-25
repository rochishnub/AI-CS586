import sys
sys.path.append("..")

from tkinter import *
from tkinter import font as tkf
from tkinter import messagebox
from minimax import best_minimax
from game import State, TicTacToe
import numpy as np
import random

S = np.zeros(9, dtype=int)
t = TicTacToe()

wins = ['Haha loserrrrrrrrrr!', 'What a moron!', "Imagine losing at a child's game..."]
loss = ['Not fair, my mom was calling', "You got lucky, won't happen again", "One word: CHEATER"]

master = Tk()
frame = Frame(master)
frame.pack(side = "right")
master.title("Tic-Tac-Toe")
# master.geometry("350x350")

font_button = tkf.Font(family="MS Sans Serif", size=50)
font_ai = tkf.Font(family="MS Sans Serif", size=20)

def play_ai():
    global t
    s = State(S)
    i = best_minimax(t, s)
    S[i] = 1

    flist = list(reversed(frame.grid_slaves()))
    f = flist[i]
    button = f.grid_slaves()[0]
    button.configure(text='X', disabledforeground='navy')
    button['state'] = 'disabled'

    check_winner()

def play_human(idx):
    S[idx] = -1
    flist = list(reversed(frame.grid_slaves()))
    f = flist[idx]
    button = f.grid_slaves()[0]
    button.configure(text='O', disabledforeground='red4')
    button['state'] = 'disabled'

    check_winner()

def check_winner():
    s = State(S)
    t = TicTacToe(with_depth=False)
    frame.update()
    winner = t.check_winner(s)
    if winner!='none':
        if winner=='draw':
            messagebox.showinfo("Draw", "It's a Tie")
        elif winner=='ai':
            messagebox.showinfo("AI wins", random.choice(wins))
        elif winner=='human':
            messagebox.showinfo("You win", random.choice(loss))

def clear():
    global S
    S = np.zeros(9, dtype=int)
    flist = list(reversed(frame.grid_slaves()))
    for f in flist[:9]:
        button = f.grid_slaves()[0]
        button.configure(text='')
        button['state'] = 'normal'

def check_depth():
    global t
    if depth.get()==1:
        t = TicTacToe()
    elif depth.get()==0:
        t = TicTacToe(with_depth=False)
    
for i in range(9):
    r,c = i//3, i%3
    f = Frame(frame, width=100, height=100)
    b = Button(f, text="", font=font_button,
               command=lambda idx=i: play_human(idx))

    f.rowconfigure(0, weight = 1)
    f.columnconfigure(0, weight = 1)
    f.grid_propagate(0)

    f.grid(row=r, column=c)
    b.grid(sticky='nsew')

f = Frame(frame, width=100, height=50)        
ai_button = Button(f, text="AI Turn", foreground='black', font=font_ai,
                   command=play_ai)
f.rowconfigure(0, weight = 1)
f.columnconfigure(0, weight = 1)
f.grid_propagate(0)
f.grid(row=4,column=1)
ai_button.grid(sticky='nsew')

f = Frame(frame, width=100, height=50)        
clear_button = Button(f, text="Clear", foreground='black', font=font_ai,
                   command=clear)
f.rowconfigure(0, weight = 1)
f.columnconfigure(0, weight = 1)
f.grid_propagate(0)
f.grid(row=4,column=2)
clear_button.grid(sticky='nsew')

depth = IntVar(frame)
f = Frame(frame, width=100, height=50)        
depth_button = Checkbutton(f, text="Depth", variable=depth, onvalue=1, offvalue=0, font=font_ai,
                           command=check_depth)
f.rowconfigure(0, weight = 1)
f.columnconfigure(0, weight = 1)
f.grid_propagate(0)
f.grid(row=4,column=0)
depth_button.grid(sticky='nsew')

mainloop()