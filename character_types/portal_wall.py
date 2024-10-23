from character_types.character import Character
from position import Position


class PortalWall(Character):

  def __init__(self, positions):
    self.positions = positions
    self.color = 'grey'
  
  def hit_by_snake(self, game, at_position):
    # Get the new position that the portal transports to
    new_position = self.get_portal_destination(game, at_position)

    # Call `hit_by_snake` on whatever character is at that new position
    game.characters.at(new_position).hit_by_snake(game, new_position)

  def get_portal_destination(self, game, position):
    # If the portal_wall is in the first column
    # return the position (in the same row) of the second to last column
    if position.x == 0:
      return Position(game.board_columns-2, position.y)

    # If the portal_wall is in the last column
    # return the position (in the same row) of the second column
    if position.x == game.board_columns-1:
      return Position(1, position.y)

    # If the portal_wall is in the first row
    # return the position (in the same column) of the second to last row
    if position.y == 0:
      return Position(position.x, game.board_rows-2)

    # If the portal_wall is in the last row
    # return the position (in the same column) of the second row
    if position.y == game.board_rows-1:
      return Position(position.x, 1)

    # Otherwise raise an error that a portal_wall is at an unexpected position
    raise ValueError(f"Invalid position for portal wall: {position}")