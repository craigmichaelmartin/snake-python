import pygame


class Graphics():
  def __init__(self, game):
    pygame.init()

    self.game = game
    self.font = pygame.font.Font(None, 25)
    self.screen = pygame.display.set_mode(self.game.board.size)
    
  def draw_text(self, text, color, x, y):
    text_image = self.font.render(text, True, color)
    self.screen.blit(text_image, ((x, y)))
  
  def draw_character(self, character):
    for position in character.positions:
      # tuple for (left, top, width, height)
      rectangle = (
        (position.x * (self.game.board.block_size + self.game.board.block_gap)) + self.game.board.border,
        (position.y * (self.game.board.block_size + self.game.board.block_gap)) + self.game.board.border,
        self.game.board.block_size,
        self.game.board.block_size
      )
      pygame.draw.rect(self.screen, character.color, rectangle)
  
  def draw_game(self):
    self.ensure_valid_state()
  
    self.screen.fill('white')
  
    self.draw_text(
      f'SCORE: {self.game.score} | HIGH SCORE: {self.game.high_score}',
      "black",
      self.game.board.border,
      self.game.board.border / 3
    )
    if self.game.game_over:
      self.draw_text(
        "GAME OVER. PRESS SPACE.",
        "Green",
        self.game.board.border,
        self.game.board.height - self.game.board.border,
      )  
    for character in self.game.characters.list:
      self.draw_character(character)
  
    pygame.display.update()
  
  def ensure_valid_state(self):
    all_positions = []
    for character in self.game.characters.list:
      for position in character.positions:
        all_positions.append(position)
    board_positions = self.game.board.rows * self.game.board.columns
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