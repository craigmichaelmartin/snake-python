from character_types.character import Character


class Wall(Character):

  def __init__(self, positions):
    self.positions = positions
    self.color = 'yellow'

  def hit_by_snake(self, game, at_position):
    game.game_over = True