import pygame
import pygame_menu
import sys
from src import ball
from src import block
from src import board
from src import utility

# Things that still need to be implemented in the controller:
  # Implement correct behavior when the ball collides with the side of a block/board
  # Add a life and score counter to the top of the window
  # Increment the score by 1 when a block is broken
  # Game over when lives reach 0

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()    
    self.utility = utility.Utility()
    self.window_width = 720
    self.window_height = 550
    self.screen = pygame.display.set_mode((self.window_width, self.window_height))
    pygame.display.set_caption("Super Block Breaker")
    self.background = pygame.Surface((self.window_width, self.window_height))
    self.background.fill((self.utility.LIGHTBLUE))

    #sets up menu variables
    menubg = pygame_menu.baseimage.BaseImage(image_path="assets/sbb_bg.png", drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER, drawing_offset=(0,85))
    menutheme = pygame_menu.Theme(background_color=menubg, title_background_color=self.utility.DARKBLUE, title_font_shadow=False, title_font=pygame_menu.font.FONT_MUNRO, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL, widget_padding=10, widget_font=pygame_menu.font.FONT_MUNRO)
    
    self.menu = pygame_menu.Menu('SUPER BLOCK BREAKER', self.window_width, self.window_height, theme=menutheme)
    self.menu.add.button('Play', self.start_game)
    self.menu.add.button('Quit', pygame_menu.events.EXIT)

    #sets up blocks
    self.blocks = pygame.sprite.Group()
    top_row = 40
    spacing = 10
    block_height = 30
    difference = spacing + block_height
    for i in range(10):
      self.blocks.add(block.Block(10 + i*70, top_row, self.utility.RED))
      self.blocks.add(block.Block(10 + i*70, top_row + difference, self.utility.BLUE))
      self.blocks.add(block.Block(10 + i*70, top_row + difference*2, self.utility.GREEN))

    # sets up paddle
    self.player = pygame.sprite.Group()
    self.board = board.Board(x=310,y=500,w=100,h=20, color=self.utility.WHITE)
    self.player.add(self.board)
    # sets up a ball
    self.ball = ball.Ball(x=280, y=400)
    self.balls = pygame.sprite.Group()
    self.balls.add(self.ball)

    # sets up score and life labels
    self.lives = 3
    self.score = 0
    pygame.font.init()
    self.font = pygame.font.SysFont(None, 30)
    self.lifedisplay = self.font.render(f'Lives: {self.lives}', False, self.utility.BLACK)
    self.scoredisplay = self.font.render(f'Score: {self.score}', False, self.utility.BLACK)
    
    #change game state to menu
    self.state = "MENU"

    #limits fps
    self.clock = pygame.time.Clock()
    self.clock.tick(60)
    
  def mainloop(self):
    while self.state:
      if self.state == "MENU":
        self.menuloop()
      elif self.state == "GAME":
        self.gameloop()
      elif self.state == "OVER":
        self.gameoverloop()
    
  def menuloop(self):
    # passes events to menu based on pygame-menu
    events = pygame.event.get()
    if self.menu.is_enabled():
        self.menu.update(events)
        self.menu.draw(self.screen)

    pygame.display.update()

  def start_game(self):
    self.state = "GAME"
 
  def gameloop(self):
    pygame.event.pump()

    #collision detection
    if self.ball.rect.x >= self.window_width or self.ball.rect.x <= 0:
      self.ball.bounce("vertical")
    elif self.ball.rect.y <= 0:
      self.ball.bounce("horizontal")
    elif self.ball.rect.y >= self.window_height:
      self.ball.bounce("horizontal")
      self.lives -= 1
      if self.lives <= 0:
        self.state = "OVER"

    if pygame.sprite.groupcollide(self.balls, self.blocks, False, True):
      self.ball.bounce("horizontal")
      self.score += 1
    elif pygame.sprite.groupcollide(self.balls, self.player, False, False):
      self.ball.bounce("horizontal")
  
    # move paddle when player presses A or D
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
      self.board.move("left")
    if keys[pygame.K_d]:
      self.board.move("right")

    # updating lives and score
    self.lifedisplay = self.font.render(f'Lives: {self.lives}', False, self.utility.BLACK)
    self.scoredisplay = self.font.render(f'Score: {self.score}', False, self.utility.BLACK)
    
    self.blocks.update()
    self.player.update()
    self.balls.update()
    self.screen.blit(self.background, (0,0))
    self.blocks.draw(self.screen)
    self.player.draw(self.screen)
    self.balls.draw(self.screen)
    self.screen.blit(self.lifedisplay, (10, 10))
    self.screen.blit(self.scoredisplay, (self.window_width-85, 10))
    pygame.display.flip()
    
  def gameoverloop(self):
    if self.lives <= 0:
      over_message = self.font.render("You lose!", False, self.utility.WHITE) 
    else:
      over_message = self.font.render("You win!", False, self.utility.WHITE)
    
    self.background.fill((self.utility.BLACK))
    self.scoredisplay = self.font.render(f'Score: {self.score}', False, self.utility.WHITE)
    scorepos = (self.window_width / 2, self.window_height / 2)
    over_message_pos = (self.window_width / 2, self.window_height / 3)
    
    self.screen.blit(self.background, (0,0))
    self.screen.blit(over_message, over_message_pos)
    self.screen.blit(self.scoredisplay, scorepos)
    pygame.display.flip()
    
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()

# def draw_text(surface, text, size, x, y, color):
#     '''draw text to screen'''
#     font = pygame.font.Font(pygame.font.match_font('arial'), size)
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x, y)
#     surface.blit(text_surface, text_rect)