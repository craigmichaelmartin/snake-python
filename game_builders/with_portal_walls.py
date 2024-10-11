from character_types.apple import Apple
from character_types.blank import Blank
from character_types.portal_wall import PortalWall
from character_types.snake import Snake
from characters import Characters
from utilities.board import Board
from utilities.position import Position
from game_builders.game_builder import GameBuilder


class WithPortalWalls(GameBuilder):

  def create(self):
    board = Board(rows=16, columns=16, block_size=20, block_gap=0, border=30)

    portal_wall_positions = []
    blank_positions = []
    snake_positions = []
    apple_positions = []
    for x in range(board.columns):
      for y in range(board.rows):
        position = Position(x, y)
        if (x == 1 and y == 1):
          snake_positions.append(position)
        elif (x == 3 and y == 3):
          apple_positions.append(position)
        elif (
          x == 0 or x == board.columns - 1 or
          y == 0 or y == board.rows - 1
        ):
          portal_wall_positions.append(position)
        else:
          blank_positions.append(position)

    blank = Blank(blank_positions)
    apple = Apple(apple_positions)
    portal_wall = PortalWall(portal_wall_positions)
    snake = Snake(snake_positions)

    characters = Characters([snake, apple, blank, portal_wall])
    return (board, characters)