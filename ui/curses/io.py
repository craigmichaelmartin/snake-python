import curses

class Io():
  def __init__(self, graphics):
    self.graphics = graphics
  def get_key(self):
    return self.graphics.screen.getch()
  def draw_game(self):
    self.graphics.draw_game()

  @property
  def KEY_UP(self):
    return curses.KEY_UP
  @property
  def KEY_DOWN(self):
    return curses.KEY_DOWN
  @property
  def KEY_LEFT(self):
    return curses.KEY_LEFT
  @property
  def KEY_RIGHT(self):
    return curses.KEY_RIGHT