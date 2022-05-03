import pygame

class Block(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.width = 50
    self.height = 30
    self.rect = pygame.rect(self.height, self.width, 0, 0)
    
 
  def blocks(self):      # Sprite groups are handeled by the controller
    block = []           # You should also be using the pygame.sprite.Group()
    def x(self):         # class instead of a list
      for x in range(x):
      block_x = 50*x
    
  def y(self):            # I don't know what these functions are for?
      for y in range(y):
      block_y = 30*y

# Should have a function to randomly determine if it drops a powerup
# (e.g. return a boolean True or False)
# Blocks should be able to be assigned a color; controller should be able
# to randomly pick a color, which is then passed to the sprite