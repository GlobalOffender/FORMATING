# Imports
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import random
from random import randrange, shuffle
from tkinter.messagebox import showinfo

Answers = []

# Start Window
root = tk.Tk()
root.title = ("Minecraft LAN Party")
root.geometry("250x355")
root.configure(bg="white")

# Exit
def Close():
    root.destroy()
root.bind('<Escape>', lambda event: Close())

# Answer retriever
def Retrieve():
    Answers.append(Question1.get())
    Answers.append(Question2.get())
    Answers.append(Question3.get())
    Answers.append(Question4.get())
    print(Answers)
    InterfaceClear()

# Answers
def InterfaceClear():
    Question1Text.destroy()
    Question1.destroy()
    Question2Text.destroy()
    Question2.destroy()
    Question3Text.destroy()
    Question3.destroy()
    Question4Text.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    Button.destroy()
    AnswerDisplay()

def AnswerDisplay():
    Symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random.shuffle(Symbols)
    Code = []
    AnswerHeader = tk.Label(root, text="Your Answers", font=('consolas', 10), bg="white")
    AnswerHeader.pack(pady=2.5, anchor="center")
    Answer1 = tk.Label(root, text=Answers[0], font=('consolas', 20), bg="white")
    Answer1.pack(pady=2.5, anchor="center")
    Answer2 = tk.Label(root, text=Answers[1], font=('consolas', 20), bg="white")
    Answer2.pack(pady=2.5, anchor="center")
    Answer3 = tk.Label(root, text=Answers[2], font=('consolas', 20), bg="white")
    Answer3.pack(pady=2.5, anchor="center")
    Answer4 = tk.Label(root, text=Answers[3], font=('consolas', 20), bg="white")
    Answer4.pack(pady=2.5, anchor="center")
    for x in range(0,10):
        Code.append(Symbols[x])
    CodeDisplay = tk.Label(root, text=Code, font=('consolas', 10), bg="white")
    CodeDisplay.pack(pady=2.5, anchor="center")
# Questions
Question1Text = tk.Label(root, text="What's your Name?", font=('consolas', 10), bg="white")
Question1Text.pack(pady=2.5, anchor="center")
Question1 = tk.Entry(root)
Question1.pack(pady=10, anchor="center")

Question2Text = tk.Label(root, text="What's your Username", font=('consolas', 10), bg="white")
Question2Text.pack(pady=2.5, anchor="center")
Question2 = tk.Entry(root)
Question2.pack(pady=10, anchor="center")

Question3Text = tk.Label(root, text="Who are you teaming with?", font=('consolas', 10), bg="white")
Question3Text.pack(pady=2.5, anchor="center")
Question3 = tk.Entry(root)
Question3.pack(pady=10, anchor="center")

Question4Text = tk.Label(root, text="What's your Faction?", font=('consolas', 10), bg="white")
Question4Text.pack(pady=2.5, anchor="center")
Question4 = tk.StringVar()
r1 = ttk.Radiobutton(root, text='Lime', value='Lime', variable=Question4)
r2 = ttk.Radiobutton(root, text='Crimson', value='Crimson', variable=Question4)
r3 = ttk.Radiobutton(root, text='Grey', value='Grey', variable=Question4)
r1.pack(pady=2.5, anchor="center")
r2.pack(pady=2.5, anchor="center")
r3.pack(pady=2.5, anchor="center")

Button = tk.Button(root)
Button.configure(font=('consolas', 10), text="Submit Answers", bg="red", fg="white", command=Retrieve)
Button.pack(pady=10, anchor="center")

# End
root.mainloop()