from character_types.character import Character


class Blank(Character):

  def __init__(self, positions):
    self.positions = positions
    self.color = 'black'

  def hit_by_snake(self, game, at_position):
    self.positions = [p for p in self.positions if p != at_position]
    game.characters.snake.positions.insert(0, at_position)
    tail_position = game.characters.snake.tail_position
    game.characters.snake.positions.pop()
    self.positions.append(tail_position)