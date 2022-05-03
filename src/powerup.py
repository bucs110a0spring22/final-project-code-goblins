import pygame

class PowerUp(pygame.sprite.Sprite):
  def __init__(self, x, y, type, image):  # Asks for the location and type of powerup
    super().__init__()
    self.image = pygame.image.load('assets/ball.png').convert_alpha()
    self.rect = self.image.get_rect()
    
# Powerup should have a function to return the type of powerup
