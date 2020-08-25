#this is where the game snake is going 

print('this is the snake game')
import tkinter as tk 
from tkinter import * 
import os
#making the gui 
root = tk.Tk()
#making size of the gui 
root.geometry("500x250")
#making the text box for the game 
text_box_1 = tk.Label(root, height = 5, width = 40, text='Pick a game you want to play.')

text_box_1.pack()

root.mainloop() #main loop 