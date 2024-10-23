from character_types.apple import Apple
from character_types.blank import Blank
from character_types.snake import Snake
from character_types.wall import Wall
from characters import Characters
from position import Position
from game_builders.game_builder import GameBuilder


class WithRegularWalls(GameBuilder):
  
  def create(self):
    # 🕵️ Try changing these numbers
    rows = 26
    columns = 26
    
    snake = Snake([Position(1,1)])
    # 🕵️ What about adding multiple positions so there are multiple apples?
    apple = Apple([Position(3,3)])
  
    wall_positions = []
    blank_positions = []
    for x in range(columns):
      for y in range(rows):
        position = Position(x, y)
        if position not in snake.positions + apple.positions:
          if (x == 0 or x == columns - 1 or y == 0 or y == rows - 1):
            wall_positions.append(position)
          else:
            blank_positions.append(position)
    blank = Blank(blank_positions)
    wall = Wall(wall_positions)
  
    characters = Characters([snake, apple, blank, wall])
    return characters