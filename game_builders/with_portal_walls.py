from character_types.apple import Apple
from character_types.blank import Blank
from character_types.wall import Wall
from character_types.portal_wall import PortalWall
from character_types.snake import Snake
from characters import Characters
from position import Position

class WithPortalWalls():

  def create(self):
    # 🕵️ Try changing these numbers
    rows = 16
    columns = 16

    # We can specify starting positions for any characters here
    snake_positions = [Position(1,1)]
    apple_positions = [Position(3,3)]
    portal_wall_positions = []
    blank_positions = []

    # We add all these positions together into one list
    taken_positions = snake_positions + apple_positions +\
      portal_wall_positions + blank_positions

    # Any positions not `taken_positions` will be filled in here
    for x in range(columns):
      for y in range(rows):
        position = Position(x, y)
        if position not in taken_positions:
          if (x == 0 or x == columns - 1 or y == 0 or y == rows - 1):
            portal_wall_positions.append(position)
          else:
            blank_positions.append(position)

    # Create each of the characters
    snake = Snake(snake_positions)
    apple = Apple(apple_positions)
    portal_wall = PortalWall(portal_wall_positions)
    blank = Blank(blank_positions)

    # Create the Characters instance
    characters = Characters([snake, apple, portal_wall, blank])

    return characters