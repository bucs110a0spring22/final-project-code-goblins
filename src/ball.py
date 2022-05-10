import pygame

class Ball(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load('assets/ball.png').convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = [1, 1]
      
  def bounce(self, axis):
    # Horizontal bounces flips the y speed
    # Vertical bounces flip the x speed
    # Reverse bounces flip both speeds

    # Originally an attempt by Software Lead to add randomness
    # to bounces. However, it was too finicky, so this was abandoned
    # if random.randrange(2):
    #   print(random.randrange(2))
    #   self.reverse_bounce()
    
    if axis == "horizontal":
      self.h_bounce()
    elif axis == "vertical":
      self.v_bounce()
      
  def h_bounce(self):
    self.speed[1] = -self.speed[1]
    self.rect.x += self.speed[0]
    self.rect.y += self.speed[1]

  def v_bounce(self):
    self.speed[0] = -self.speed[0]
    self.rect.x += self.speed[0]
    self.rect.y += self.speed[1]

  def reverse_bounce(self):
    self.speed[0] = -self.speed[0]
    self.speed[1] = -self.speed[1]
    self.rect.x += self.speed[0]
    self.rect.y += self.speed[1]
    
  def update(self):
    self.rect.x += self.speed[0]
    self.rect.y += self.speed[1]

# Software Lead: Has a bug where bounces against the sides of objects
# (especially the board) are not handled correctly.
# Difficult to fix, as pygame does not have a function
# To determine which side of a rectangle
# you are hitting
    
    
  
