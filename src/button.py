import pygame

class Button(pygame.sprite.Sprite):

  def __init__():
    super().__init__()
    
  def StartEnd_game():                                  
    key = pygame.key.press()    # Event interpretation is handeled by 
    if key[pygame.K_Space]:     # the controller; consider instead
      run = True                # writing a functions that sets some
    elif key[pygame.K_Escape]:  # self.toggle to True or False
      run = False
    pygame.event.pump()