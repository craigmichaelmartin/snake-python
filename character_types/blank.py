import random
from character_types.character import Character


class Blank(Character):

  def __init__(self, positions):
    self.positions = positions
    self.color = 'black'

  def hit_by_snake(self, game, at_position):
    # Remove the `at_position` from the blank's list of positions
    self.positions = [p for p in self.positions if p != at_position]

    # Add the `at_position` to the snakes body
    game.characters.snake.positions.insert(0, at_position)

    # Get the snake's tail position
    tail_position = game.characters.snake.tail_position

    # Remove the last position of the snake's body
    game.characters.snake.positions.pop()

    # Add the position of what was the snake's tail to the list of
    # blank's positions
    self.positions.append(tail_position)

  def get_random_position(self):
    return random.choice(self.positions)