
import tkinter as tk
from tkinter import filedialog, Text
import os
import time

root = tk.Tk()
root.title("I'm a little cat boy")

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="#517574")

label = tk.Label(root, fg="green")
label.pack()


startButton = tk.Button(root, text="plant your tree.", padx=8, pady=10, fg="white", bg="#263D42")
stopButton = tk.Button(root, text="kill your tree.", padx=14, pady=10, fg="white", bg="#263D42", command=root.destroy)


startButton.pack()
stopButton.pack()

pushbutton.startButton()



root.mainloop()