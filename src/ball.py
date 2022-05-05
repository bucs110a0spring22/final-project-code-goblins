import pygame

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('assets/ball.png').convert_alpha()
    self.rect = self.image.get_rect()
    self.speed = [0, 5]
      
  def bounce(self, axis):
    # Horizontal bounces flips the y speed
    # Vertical bounces flip the x speed
    if axis == "horizontal":
      self.speed[1] = -self.speed[1]
    elif axis == "vertical":
      self.speed[0] = -self.speed[0]
      
  def update(self):
    self.rect.move(self.speed)

# Collisions should be handled by the controller
    
    
  
