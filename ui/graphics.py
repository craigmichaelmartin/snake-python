import pygame


class Graphics():
  def __init__(self, game):
    pygame.init()

    self.game = game
    self.block_size = 20
    self.block_gap = 0
    self.border = 30
  
    self.font = pygame.font.Font(None, 25)
    self.screen = pygame.display.set_mode((
      self.game.board_columns * (self.block_size + self.block_gap) + (self.border * 2),
      (self.game.board_rows + 1) * (self.block_size + self.block_gap) + (self.border * 2)
    ))
    
  def draw_text(self, text, color, x, y):
    text_image = self.font.render(text, True, color)
    self.screen.blit(text_image, ((x, y)))
  
  def draw_character(self, character):
    for position in character.positions:
      # tuple for (left, top, width, height)
      rectangle = (
        (position.x * (self.block_size + self.block_gap)) + self.border,
        ((self.game.board_rows - position.y +1) * (self.block_size + self.block_gap)),
        self.block_size,
        self.block_size
      )
      pygame.draw.rect(self.screen, character.color, rectangle)
  
  def draw_game(self):
    self.ensure_valid_state()
  
    self.screen.fill('white')
  
    self.draw_text(
      f'SCORE: {self.game.characters.score} | HIGH SCORE: {self.game.high_score}',
      "black",
      self.border,
      self.border / 3
    )
    if self.game.game_over:
      self.draw_text(
        "GAME OVER. PRESS SPACE.",
        "black",
        self.border,
        self.game.board_rows * (self.block_size + self.block_gap) + (self.border * 2),
      )  
    for character in self.game.characters.list:
      self.draw_character(character)
  
    pygame.display.update()
  
  def ensure_valid_state(self):
    all_positions = []
    for character in self.game.characters.list:
      for position in character.positions:
        all_positions.append(position)
    board_positions = self.game.board_rows * self.game.board_columns
    if len(all_positions) != board_positions:
      raise ValueError(
        f"Characters occupy {len(all_positions)} positions "
        f"but the board has {board_positions} positions."
        f"The character list is: {self.game.characters.list}"
      )
    if len(set(all_positions)) != len(all_positions):
      raise ValueError(
        f"The same position is occupied more than once."
        f"The character list is: {self.game.characters.list}"
      )