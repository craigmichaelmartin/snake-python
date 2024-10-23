from character_types.blank import Blank
from character_types.snake import Snake
from character_types.character import Character

class Characters:

  def __init__(self, list: list[Character]):
    self.list = list

  def at(self, position):
    # Returns the character who is at the position
    return next(filter(lambda c: position in c.positions, self.list))

  @property
  def snake(self):
    # Returns the snake character from the list of characters
    return next(filter(lambda c: isinstance(c, Snake), self.list))

  @property
  def blank(self):
    # Returns the blank character from the list of characters
    return next(filter(lambda c: isinstance(c, Blank), self.list))

  @property
  def score(self):
    # Returns the score of all characters combine
    score = 0
    for character in self.list:
      score = score + character.score
    return score