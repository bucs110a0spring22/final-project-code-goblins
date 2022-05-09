import pygame

class Board(pygame.sprite.Sprite):

  def __init__(self, x=0, y=0, w=100, h=20, color=(0,0,0)):
    super().__init__()
    self.color = color
    self.h = h
    self.w = w
    self.image = pygame.Surface((self.w, self.h))
    self.image.fill((color))
    self.rect = pygame.Rect(x, y, self.w, self.h)

  def move(self, direction):                       
    if direction == "left":
      self.rect.x -= 1
    if direction == "right":
      self.rect.x += 1
      
    #change starting pos and speed depending on screen size (note to self)
    # Note by Software Lead: I don't think it has to be that complicated;
    # or rather, we should probably get the game up and running before we
    # worry about how well it runs when resized
