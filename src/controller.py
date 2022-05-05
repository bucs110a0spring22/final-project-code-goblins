import pygame
import pygame_menu
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
    self.utility = utility.Utility()
    
    self.window_width = 720
    self.window_height = 720
    self.screen = pygame.display.set_mode((self.window_width, self.window_height))
    pygame.display.set_caption("Super Block Breaker")
    self.background = pygame.Surface((self.window_width, self.window_height))
    self.background.fill((self.utility.LIGHTBLUE))

    #sets up menu variables
    menubg = pygame_menu.baseimage.BaseImage(image_path="assets/sbb_bg.png", drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER)
    menutheme = pygame_menu.Theme(background_color=menubg, title_background_color=self.utility.DARKBLUE, title_font_shadow=False, title_font=pygame_menu.font.FONT_MUNRO, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL, widget_padding=10, widget_font=pygame_menu.font.FONT_MUNRO)
    
    self.menu = pygame_menu.Menu('SUPER BLOCK BREAKER', 720, 720, theme=menutheme)
    self.menu.add.button('Play', self.start_game)
    self.menu.add.button('Quit', pygame_menu.events.EXIT)

    #change game state to menu
    self.state = "MENU"
 
    
    #fps: #pygame.time.Clock()
    #run = True
    #while run:
      #pygame.time(60)
    
  def mainloop(self):
    while self.state:
      if self.state == "MENU":
        self.menuloop()
      elif self.state == "GAME":
        self.gameloop()
      elif self.state == "OVER":
        self.gameoverloop()
    
  def menuloop(self):
    events = pygame.event.get()
    if self.menu.is_enabled():
        self.menu.update(events)
        self.menu.draw(self.screen)

    pygame.display.update()

  def start_game(self):
    self.state = "GAME"
 
  def gameloop(self):
    self.blocks = pygame.sprite.Group()
    for i in range(10):
      self.blocks.add(block.Block(10 + i*70, 10, self.utility.RED))
      self.blocks.add(block.Block(10 + i*70, 45, self.utility.BLUE))
      self.blocks.add(block.Block(10 + i*70, 80, self.utility.GREEN))

      #update data

      #redraw
    while True:
      self.screen.blit(self.background, (0,0))
      self.blocks.draw(self.screen)
      
      pygame.display.flip()
    
  def gameoverloop(self):
    pass  
    #event loop

      #update data

      #redraw
