import pygame

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('assets/ball.png').convert_alpha()
    self.rect = self.image.get_rect()
    self.speed = [0, 5]
      
  def bounce(self, axis):
    if axis == "horizontal":            # Horizontal bounces flips the y speed
      self.speed[1] = -self.speed[1]
    elif axis == "vertical":            # Vertical bounces flip the x speed
      self.speed[0] = -self.speed[0]
      
  def update(self):
    self.rect.move(self.speed)
    
    
  
