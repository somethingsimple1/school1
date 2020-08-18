import tkinter as tk 
from tkinter import * 
import os

#making the gui 
root = tk.Tk()
#making size of the gui 
root.geometry("500x250")

#opening the guessing game
def Guessing_game():
  os.system('python Games/Guessing.py')

#opening the snake game 
def Snake_game(): 
  os.system('python Games/guessing.py')

#making the text box for the game 
text_box_1 = tk.Label(root, height = 5, width = 40, text='Pick a game you want to play.')

#the buttons for the game 
Button_Game1 = Button(root, text='Guessing game', command=Guessing_game )
Button_Game2 = Button(root, text='snake game', command=Snake_game )
Button_Game3 = Button(root, text='3', )

#packing the buttons in the the gui 
text_box_1.pack() 
Button_Game1.pack()
Button_Game2.pack()
Button_Game3.pack()




#the dictionary of all 5 games 
Dic_Games = { 
'Game1' : {'game1', '1', 'guessing game'},
'Game2' : {'game2', '2', 'snake'},
'Game3' : {'game3', '3',},
}














root.mainloop() #main loop 




