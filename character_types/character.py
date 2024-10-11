import random
from abc import ABC
from typing import List

from utilities.position import Position


# This is the base class that all character types extend.
class Character(ABC):
  positions: List[Position]

  def update(self, game):
    return  # By default objcts don't update

  def hit_by_snake(self, game, at_position):
    return  # By default nothing happens when an object is hit by a snake

  def score(self) -> int:
    return 0  # By default characters don't impact the score

  def handle_user_interaction(self, key, pygame):
    return

  def get_random_position(self):
    return random.choice(self.positions)

  def __repr__(self):
    return f"<{self.__class__.__name__} positions:{self.positions}>"
  
  def __str__(self):
    return f"<{self.__class__.__name__} positions:{self.positions}>"