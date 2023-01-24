import os
import sys
import random
import keyboard
from tkinter import *
import tkinter.messagebox as messagebox


def get_random_file(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    if len(files) == 1:
        messagebox.showerror("Error", "Need some files")
        sys.exit()
    file = random.choice(files)
    while os.path.splitext(file)[1] == '.exe':
        file = random.choice(files)
    return file


def open_file():
    path = os.getcwd()
    random_file = get_random_file(path)
    os.startfile(random_file)


root = Tk()
root.attributes("-topmost",True)
root.geometry("200x30")
root.resizable(False, False)
root.title(":)")

keyboard.add_hotkey('ctrl+alt+shift+o', open_file)

button = Button(root, text="Open Random File", command=open_file)
button.pack()

root.mainloop()
