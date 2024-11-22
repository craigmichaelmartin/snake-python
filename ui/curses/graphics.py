import curses
from ui.curses.io import Io

class Graphics():
  def __init__(self, Game):
    self.Game = Game
    curses.wrapper(self.setup)

  def setup(self, screen):
    self.screen = screen
    self.game = self.Game(Io(self))
    self.setup_colors()
    curses.curs_set(0)
    self.screen.keypad(1)
    curses.noecho()
    curses.cbreak()
    self.screen.nodelay(1)
    self.game.start_game_loop()

  def draw_game(self):
    self.screen.clear()
    self.draw_score_text()
    self.draw_characters()
    self.draw_game_over_text()
    self.screen.refresh()

  def draw_score_text(self):
    score_text = f'SCORE: {self.game.characters.score}'
    high_score_text = f'HIGH: {self.game.high_score}'
    self.draw_text(0, 0, score_text)
    self.draw_text(
      (self.game.board_columns * 2) - len(high_score_text),
      0,
      high_score_text
    )

  def draw_game_over_text(self):
    if self.game.game_over:
      game_over_text = "GAME OVER. PRESS SPACE."
      self.draw_text(
        ((self.game.board_columns * 2) - len(game_over_text)) // 2,
        (self.game.board_rows // 2) + 1,
        game_over_text
      )

  def draw_characters(self):
    for character in self.game.characters.list:
      self.draw_character(character)

  def draw_character(self, character):
    for position in character.positions:
      self.draw_text(
        position.x * 2,
        self.game.board_rows - position.y + 1,
        '██',
        self.colors[character.color]
      )

  def draw_text(self, x, y, text, color_pair=0):
    try:
      if color_pair:
        self.screen.attron(curses.color_pair(color_pair))
      self.screen.addstr(y, x, text)
      if color_pair:
        self.screen.attroff(curses.color_pair(color_pair))
    except curses.error:
        pass

  def setup_colors(self):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    self.colors = {
      "green": 1,
      "red": 2,
      "white": 3,
      "blue": 4,
      "yellow": 5,
      "black": 6,
      "cyan": 7,
      "magenta": 8
    }