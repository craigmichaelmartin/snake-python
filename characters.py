from character_types.blank import Blank
from character_types.snake import Snake


class Characters:

  def __init__(self, list):
    self.list = list

  def at(self, position):
    return next(filter(lambda c: position in c.positions, self.list))

  @property
  def snake(self):
    return next(filter(lambda c: isinstance(c, Snake), self.list))

  @property
  def blank(self):
    return next(filter(lambda c: isinstance(c, Blank), self.list))

  def score(self):
    score = 0
    for character in self.list:
      score = score + character.score()
    return score