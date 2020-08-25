import tkinter as tk 
from tkinter import * 
from Games.Guessing import welcome 
import constants




if __name__ == "__main__": 
  #making the gui 
  root = tk.Tk()
  root.title("My Games")

  
  #making the frame 
  label = tk.Frame(root, width=35, height=240, padx=constants.layout["pad_x"], pady=constants.layout["pad_y"])

  tk.Label(label, text="Pick the game you want to play.").grid()



  label.grid(column=0, row=0)

    

  #the buttons for the game 
  buttons = tk.Frame(root, width=35, height=240)

  tk.Button(buttons, text='Guessing game').grid()
  tk.Button(buttons, text='snake game').grid()
  tk.Button(buttons, text='Flappy bird').grid()

  buttons.grid(column=0, row=1)

  root.mainloop() 


