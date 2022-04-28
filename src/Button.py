import pygame

def StartEnd_game():
  
  key = pygame.key.press()
  
  if key[pygame.K_Space]:
    run = True
  elif key[pygame.K_Escape]:
    run = False
  pygame.event.pump()