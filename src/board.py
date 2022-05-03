import pygame 

class Board(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.height = 20
    self.width = 100
    self.x = 0
    self.y = 0
    self.speed = 20
    self.rect = pygame.rect(self.height, self.width, self.x, self.y)

  def move_board(self):                       # Event interpretation
    self.direction = 0                        # should be handeled by the
    key = pygame.key.press()                  # controller
    if key[pygame.A] and self.rect.A > 0:
      self.direction = -1
    if key[pygame.D] and self.rect.D < 0:
      self.direction = 1
      
    #change starting pos and speed depending on screen size (note to self)
    # Note by Software Lead: I don't think it has to be that complicated;
    # or rather, we should probably get the game up and running before we
    # worry about how well it runs when resized
