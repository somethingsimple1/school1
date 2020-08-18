

from tkinter import *
root = Tk()



"""
#making a lable widget 
mylabel = Label(root, text='hello world')

#packing the widet on to the screen 
mylabel.pack() 
"""


""" 
#using grids 

# maiking the lables widets 
mylabel1 = Label(root, text='hello world')
mylabel2 = Label(root, text='this is the widget 2')

#packing the Widgets on screen 
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)
""" 



#making the button say 'look i clicked a button' - note the function must be before the button 
def myclick(): 
  mylabel = Label(root, text='look i clicked a button')
  mylabel.pack() 


#making a button 
#use 'pady' and 'payx' to add padding to the button 
mybutton = Button(root, text='click me', padx=50, command=myclick, fg='blue')

#packing the Widgets on screen 
mybutton.pack()





















root.mainloop() #main loop 

