from tkinter import * 
import os 
root = Tk()

#opening the guessing game
def Guessing_game():
  os.system('python Games/Guessing.py')

#opening the snake game 
def Snake_game(): 
  os.system('python Games/guessing.py')



#the buttons for the game 
Button_Game1 = Button(root, text='Guessing game', command=Guessing_game )
Button_Game2 = Button(root, text='snake game', command=Snake_game )
Button_Game3 = Button(root, text='3', )

#packing the buttons in the the gui 
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




