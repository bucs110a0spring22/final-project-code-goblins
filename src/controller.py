import pygame
import sys
from src import ball
from src import block
from src import board
from src import utility

import pygame
import sys


# Things that the controller should be able to do:
#   Initialize the screen (width, height, background)
#   Set up all the blocks and add them into a sprite groups
#   Add the player character at the bottom of the screen
#   Add a ball, and throw it towards the player character
#   Bounce the ball once it detects a collision with another sprite
#   


class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()    
    self.window_width = 720
    self.window_height = 720
    self.screen = pygame.display.set_mode((self.window_width, self.window_height))
    self.utility = utility.Utility()
    
    #fps: #pygame.time.Clock()
    #run = True
    #while run:
      #pygame.time(60)
    
  def mainloop(self):
    self.gameloop()
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    pass

      
  def gameloop(self):
    self.blocks = pygame.sprite.Group()
    for i in range(10):
      self.blocks.add(block.Block(10 + i*70, 10, self.utility.RED))
      self.blocks.add(block.Block(10 + i*70, 45, self.utility.BLUE))
      self.blocks.add(block.Block(10 + i*70, 80, self.utility.GREEN))

      #update data

      #redraw
    while True:
      self.blocks.draw(self.screen)
      pygame.display.flip()
    
  def gameoverloop(self):
    pass  
    #event loop

      #update data

      #redraw
