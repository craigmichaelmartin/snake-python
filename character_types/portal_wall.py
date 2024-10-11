from character_types.character import Character
from utilities.position import Position


class PortalWall(Character):

  def __init__(self, positions):
    self.positions = positions
    self.color = 'yellow'
  
  def hit_by_snake(self, game, at_position):
    new_position = self.get_portal_destination(game, at_position)
    game.characters.at(new_position).hit_by_snake(game, new_position)

  def get_portal_destination(self, game, position):
    if position.x == 0:
      return Position(game.board.columns-2, position.y)
    elif position.x == game.board.columns-1:
      return Position(1, position.y)
    elif position.y == 0:
      return Position(position.x, game.board.rows-2)
    elif position.y == game.board.rows-1:
      return Position(position.x, 1)
    else:
      raise ValueError(f"Invalid position for portal wall: {self.position}")