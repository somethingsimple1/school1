import tkinter as tk 
import constants 



class Master(tk.Canvas):

  #making the canvas 
  def __init__(self, b): 
    super().__init__(b)

    #configuring the size and color of the canvas 
    self.configure(
      width=constants.layout["canvas_size"],
      height=constants.layout["canvas_size"],
      bg=constants.layout["background_color"]
    )