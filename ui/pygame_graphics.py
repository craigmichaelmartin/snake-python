import pygame


class Graphics():
  def __init__(self, on_ready):
    pygame.init()
    on_ready(self)

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

  def game_specific_setup(self, game):
    self.block_size = 20
    self.block_gap = 0
    self.border = 30
    self.font = pygame.font.Font(None, 25)
    self.screen = pygame.display.set_mode((
      game.board_columns * (self.block_size + self.block_gap) + (self.border * 2),
      (game.board_rows + 1) * (self.block_size + self.block_gap) + (self.border * 2)
    ))

  def get_key(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        return event.key

  def draw_game(self, game):
    self.screen.fill('white')

    self.draw_text(
      f'SCORE: {game.characters.score} | HIGH SCORE: {game.high_score}',
      "black",
      self.border,
      self.border / 3
    )
    if game.game_over:
      self.draw_text(
        "GAME OVER. PRESS SPACE.",
        "black",
        self.border,
        game.board_rows * (self.block_size + self.block_gap) + (self.border * 2),
      )
    for character in game.characters.list:
      self.draw_character(character, game)

    pygame.display.update()


  def draw_text(self, text, color, x, y):
    text_image = self.font.render(text, True, color)
    self.screen.blit(text_image, ((x, y)))

  def draw_character(self, character, game):
    for position in character.positions:
      # tuple for (left, top, width, height)
      rectangle = (
        (position.x * (self.block_size + self.block_gap)) + self.border,
        ((game.board_rows - position.y +1) * (self.block_size + self.block_gap)),
        self.block_size,
        self.block_size
      )
      pygame.draw.rect(self.screen, character.color, rectangle)