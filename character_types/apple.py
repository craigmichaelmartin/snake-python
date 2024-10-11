from character_types.character import Character


class Apple(Character):

  def __init__(self, positions):
    self.positions = positions
    self.color = 'dark red'

  def hit_by_snake(self, game, at_position):
    self.positions = [p for p in self.positions if p != at_position]
    game.characters.snake.positions.insert(0, at_position)
    random_position = game.characters.blank.get_random_position()
    game.characters.blank.positions = \
      [p for p in game.characters.blank.positions if p != random_position]
    self.positions.append(random_position)