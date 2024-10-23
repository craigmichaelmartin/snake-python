from typing import List
from position import Position


# This is the base class that all character types extend.
class Character():
  positions: List[Position]

  @property
  def score(self) -> int:
    # By default characters don't impact the score
    return 0

  def update(self, game):
    # By default objcts don't update
    return

  def hit_by_snake(self, game, at_position):
    # By default nothing happens when an object is hit by a snake
    return

  def handle_user_interaction(self, key, pygame):
    # By default characters don't respond to user interactions
    return

  def __repr__(self):
    return f"<{self.__class__.__name__} positions:{self.positions}>"
  
  def __str__(self):
    return f"<{self.__class__.__name__} positions:{self.positions}>"