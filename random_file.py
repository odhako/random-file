import os
import random
import keyboard
from tkinter import *


def get_random_file(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return random.choice(files)


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
