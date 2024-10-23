from character_types.character import Character


class Apple(Character):

  def __init__(self, positions):
    self.positions = positions
    # 🐛 BUG LOCATION 🐛
    # We want Apple instances to have a color of red
    self.color = 'white'

  def hit_by_snake(self, game, at_position):
    # Remove the `at_position` from the apple's list of positions
    self.positions = [p for p in self.positions if p != at_position]

    # Add the `at_position` to the snakes body
    game.characters.snake.positions.insert(0, at_position)

    # Get a random blank position
    random_position = game.characters.blank.get_random_position()

    # Remove this random position from the blank's list of positions
    game.characters.blank.positions = \
      [p for p in game.characters.blank.positions if p != random_position]
    
    # Add this random position to the apple's list of positions
    self.positions.append(random_position)