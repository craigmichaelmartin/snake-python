import pygame
from ui.pygame.io import Io


class Graphics():
  def __init__(self, Game):
    pygame.init()
    self.game = Game(Io(self))
    self.setup()

  def setup(self):
    self.block_size = 20
    self.block_gap = 0
    self.border = 30

    self.font = pygame.font.Font(None, 25)
    self.screen = pygame.display.set_mode((
      self.game.board_columns * (self.block_size + self.block_gap) + (self.border * 2),
      (self.game.board_rows + 1) * (self.block_size + self.block_gap) + (self.border * 2)
    ))
    self.game.start_game_loop()

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