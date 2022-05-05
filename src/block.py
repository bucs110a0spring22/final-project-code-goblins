import pygame

class Block(pygame.sprite.Sprite):
  def __init__(self, x, y, color):
    super().__init__()
    self.width = 65
    self.height = 30
    self.image = pygame.Surface((self.width, self.height))
    self.image.fill((color))

    self.rect = pygame.Rect(x, y, self.width, self.height)
    # self.rect = self.image.get_rect()
    # self.rect.x = x
    # self.rect.y = y


# No longer a need to add a function for powerups; project progress
# delayed for too long, no time to implement
# Blocks should be able to be assigned a color; controller should be able
# to pick a color, which is then passed to the sprite
# Can either leave to controller to pass RBG values, or allow the controller
# to pass a string like "RED" or "BLUE" and set color accordingly