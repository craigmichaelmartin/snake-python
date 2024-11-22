import pygame

class Io():
  def __init__(self, graphics):
    self.graphics = graphics
  def get_key(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        return event.key
  def draw_game(self):
    self.graphics.draw_game()

  @property
  def KEY_UP(self):
    return pygame.K_UP
  @property
  def KEY_DOWN(self):
    return pygame.K_DOWN
  @property
  def KEY_LEFT(self):
    return pygame.K_LEFT
  @property
  def KEY_RIGHT(self):
    return pygame.K_RIGHT