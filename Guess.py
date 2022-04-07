# Imports
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import random
from random import randrange, shuffle
from tkinter.messagebox import showinfo

Score = 0
def Program():
    # Start Window
    StartWindow = tk.Tk()
    StartWindow.title = ("Guess the word")
    StartWindow.geometry("300x200")
    StartWindow.configure(bg="white")
    Letters = []
    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # Word Retriever
    def Retrieve():
        global Length, Letters
        A = WordInput.get()
        Length = len(A)
        Letters = list(A.upper())
        Guess()
    # Spinbox Summon
    def Guess():
        global Length, relyrange, Letters, textvar, Spinbox, textList
        textList = []
        relyrange = .1
        Position = 0
        StartText.destroy()
        WordInput.destroy()
        WordInputButton.destroy()
        for x in range(0, Length):
            textvar = tk.StringVar()
            textList.append(textvar)
            List1 = []
            List1.append(Letters[Position])
            for x in range (0, 4):
                i = randrange(len(Alphabet))
                List1.append(Alphabet[i])
            shuffle(List1)
            Spinbox = tk.Spinbox(StartWindow, textvariable=textList[Position], values=List1)
            Spinbox.place(rely=relyrange, relx=0.5, anchor="center")
            relyrange = relyrange + 0.1
            Position = Position + 1
        GuessButton = tk.Button(StartWindow)
        GuessButton.configure(font=('consolas', 10), text="Submit Guess", bg="red", fg="white",command=GuessPrint)
        GuessButton.place(rely=.85, relx=.5, anchor="center")

    # Print
    def GuessPrint():
        global Length, Letters, Score
        Answer = []
        for x in range(0, Length):
            Answer.append(textList[x].get())
        if (Answer==Letters):
            Score = Score + (Length * Length)
            print("You're earned " + str(Length) + " points!")
            Confirm()
        if (Answer!=Letters):
            print("Wrong!")
            Confirm()

    # Retry
    def Confirm():
        global Score
        answer = tkinter.messagebox.askquestion(title="Game Over", message="Your score is " + str(Score) + ". Do you want to try again?")
        if answer == "yes":
            StartWindow.destroy()
            Program()
        if answer == "no":
            StartWindow.destroy()
            exit()

    # Start Components
    StartText = tk.Label(StartWindow, text="Input a word", font=('consolas', 20), bg="white")
    StartText.place(rely=.25, relx=.5, anchor="center")

    WordInput = tk.Entry(StartWindow, text="30")
    WordInput.place(rely=.5, relx=.5, anchor="center")

    WordInputButton = tk.Button(StartWindow)
    WordInputButton.configure(font=('consolas', 10), text="Submit Word", bg="red", fg="white",command=Retrieve)
    WordInputButton.place(rely=.65, relx=.5, anchor="center")

    # Exit
    def Close():
        StartWindow.destroy()
    StartWindow.bind('<Escape>', lambda event: Close())

    # End
    StartWindow.mainloop()

Program()