from character_types.character import Character


class Wall(Character):

  def __init__(self, positions):
    self.positions = positions
    self.color = 'yellow'

  def hit_by_snake(self, game, at_position):
    # When the snake's next position is a wall the game is over
    game.game_over = True