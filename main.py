import os 
from tkinter import * 
root = Tk()

def Guessing_game:
  os.system('python games/GuessingGame.py')


Button_Game1 = Button(root, text='Guessing game', command=Guessing_game )
Button_Game2 = Button(root, text='snake', )
Button_Game3 = Button(root, text='3', )
Button_Game4 = Button(root, text='4', )
Button_Game5 = Button(root, text='5', )

Button_Game1.pack()
Button_Game2.pack()
Button_Game3.pack()
Button_Game4.pack()
Button_Game5.pack()



#the dictionary of all 5 games 
Dic_Games = { 
'Game1' : {'game1', '1', 'guessing game'},
'Game2' : {'game2', '2', 'snake'},
'Game3' : {'game3', '3',},
'Game4' : {'game4', '4',},
'Game5' : {'game5', '5',}
}















root.mainloop() #main loop 




