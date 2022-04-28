import pygame 

class Board():
  def __init__(self):
    self.height = 20
    self.width = 100
    self.x = 0
    self.y = 0
    self.speed = 20
    self.shape = pygame.rect(self.height, self.width, self.x, self.y)

  def move_board(self):
    self.direction = 0
    key = pygame.key.press()
    if key[pygame.A] and self.rect.A > 0:
      self.direction = -1
    if key[pygame.D] and self.rect.D < 0:
      self.direction = 1
      
    #change starting pos and speed depending on screen size (note to self)
