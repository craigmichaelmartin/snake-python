import curses

class Graphics():
  def __init__(self, on_ready):
    curses.wrapper(self.setup, on_ready)
    
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

  def game_specific_setup(self, _game):
    pass

  def get_key(self):
    return self.screen.getch()

  def draw_game(self, game):
    self.screen.clear()
    self.draw_score_text(game)
    self.draw_characters(game)
    self.draw_game_over_text(game)
    self.screen.refresh()
    

  def setup(self, screen, on_ready):
    self.screen = screen
    self.setup_colors()
    curses.curs_set(0)
    self.screen.keypad(1)
    curses.noecho()
    curses.cbreak()
    self.screen.nodelay(1)
    on_ready(self)

  def draw_score_text(self, game):
    score_text = f'SCORE: {game.characters.score}'
    high_score_text = f'HIGH: {game.high_score}'
    self.draw_text(0, 0, score_text)
    self.draw_text(
      (game.board_columns * 2) - len(high_score_text),
      0,
      high_score_text
    )

  def draw_game_over_text(self, game):
    if game.game_over:
      game_over_text = "GAME OVER. PRESS SPACE."
      self.draw_text(
        ((game.board_columns * 2) - len(game_over_text)) // 2,
        (game.board_rows // 2) + 1,
        game_over_text
      )

  def draw_characters(self, game):
    for character in game.characters.list:
      self.draw_character(character, game)

  def draw_character(self, character, game):
    for position in character.positions:
      self.draw_text(
        position.x * 2,
        game.board_rows - position.y + 1,
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