import tkinter as tk 
import constants 


class Master(tk.Canvas):

  def __init__(self, b): 
    super().__init__(b)
    self.configure(
      width=constants.layout["canvas_size"],
      height=constants.layout["canvas_size"],
      bg=constants.layout["background_color"]
    )