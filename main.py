import tkinter as tk 
from tkinter import * 
import constants
import canvas


#making the gui 
root = tk.Tk()
root.title("My Games")

#this is for Debuging 
print("__main__")
print(__name__)



if __name__ == "__main__": 
m          
  def clear():
    main_menu_grid.destroy() 
  


  #adding the canvas to the main window 
  game_area = 


  global main_menu_grid
  main_menu_grid = tk.Frame(root, width=constants.layout["width"], height=constants.layout["height"], padx=constants.layout["pad_x"], pady=constants.layout["pad_y"])



  #making the label and adding them to the frame 
  tk.Label(main_menu_grid, text="Enter in your name").grid()
  tk.Entry(main_menu_grid, text="what is your name?").grid(pady=10) 

  #making the buttons and adding them to the frame 
  tk.Label(main_menu_grid, text="What game do you what to play").grid(pady=10)   

  tk.Button(main_menu_grid, text='Guessing game').grid()
  tk.Button(main_menu_grid, text='snake game').grid()
  tk.Button(main_menu_grid, text='Flappy bird').grid()


  #adding the fram called "label" to the grid 
  main_menu_grid.grid(column=0, row=0)

    

#getting user name




  root.mainloop() 
  

