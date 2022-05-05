import pygame

class Board(pygame.sprite.Sprite):

  def __init__(self, x, y, w, h, color):
    super().__init__()
    self.color = (0, 0, 0)
    self.h = 20
    self.w = 100
    self.x = 0
    self.y = 0
    self.rect = pygame.rect(self.h, self.w, self.x, self.y)

  def move_board(self, direction):                       
    if direction == le and self.rect.A > 0:
      self.direction = -1
    if key[pygame.D] and self.rect.D < 0:
      self.direction = 1
      
    #change starting pos and speed depending on screen size (note to self)
    # Note by Software Lead: I don't think it has to be that complicated;
    # or rather, we should probably get the game up and running before we
    # worry about how well it runs when resized
