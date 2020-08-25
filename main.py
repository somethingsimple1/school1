import tkinter as tk 
from tkinter import * 
from Games.Guessing import welcome 
import constants




if __name__ == "__main__": 
  #making the gui 
  root = tk.Tk()
  root.title("My Games")

  
  #making the frame called "label" 
  label = tk.Frame(root, width=35, height=240, padx=constants.layout["pad_x"], pady=constants.layout["pad_y"])

  #making the label and adding them to the frame 
  tk.Label(label, text="Pick the game you want to play.").grid()


  #adding the fram called "label" to the grid 
  label.grid(column=0, row=0)

    

  #making the frame calleed "buttons"
  buttons = tk.Frame(root, width=35, height=240)

  #making the buttons and adding them to the frame 
  tk.Button(buttons, text='Guessing game').grid()
  tk.Button(buttons, text='snake game').grid()
  tk.Button(buttons, text='Flappy bird').grid()

  #addig the frame called "buttons" to the grid
  buttons.grid(column=0, row=1)


  

  root.mainloop() 


