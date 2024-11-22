class Position:

  def __init__(self, x, y):
    # A position instance has an `x` (which column it is in)
    # and a `y (which row it is in).
    # A bigger `x` means it is further to the right, a bigger `y`
    # means it is higher up
    # Here is what a graph of some positions looks like.
    # The first number is the `x` and the second is the `y`.
    #  ↑       ↑       ↑       ↑       ↑       ↑ 
    #  ├───────┼───────┼───────┼───────┼───────┼→
    #  | (0,4) | (1,4) | (2,4) | (3,4) | (4,4) |
    #  ├───────┼───────┼───────┼───────┼───────┼→
    #  | (0,3) | (1,3) | (2,3) | (3,3) | (4,3) |
    #  ├───────┼───────┼───────┼───────┼───────┼→
    #  | (0,2) | (1,2) | (2,2) | (3,2) | (4,2) |
    #  ├───────┼───────┼───────┼───────┼───────┼→
    #  | (0,1) | (1,1) | (2,1) | (3,1) | (4,1) |
    #  ├───────┼───────┼───────┼───────┼───────┼→
    #  | (0,0) | (1,0) | (2,0) | (3,0) | (4,0) |
    #  └───────┴───────┴───────┴───────┴───────┴→
    self.x = x
    self.y = y

  def __eq__(self, other):
    if isinstance(other, Position):
      return self.x == other.x and self.y == other.y
    return False
  
  def __hash__(self):
    return hash((self.x, self.y))

  def __repr__(self):
    return f"<Position(x:{self.x}, y:{self.y})>"

  def __str__(self):
    return f"<Position(x:{self.x}, y:{self.y})>"

# The game is created having characters occupy positions.
# To be valid, these occupied positions need to create
# a rectangle with no gaps.
#
# As you can see by looking at any of the character classes,
# each character has a list of positions.
#    
# The game builders are in charge of setting up the game by
# creating character instances with positions as desired.
#
# For example, a game builder might build characters to
# fill a 5x5 board. This is how the positions look:
# ┌───────┬───────┬───────┬───────┬───────┐
# | (0,4) | (1,4) | (2,4) | (3,4) | (4,4) |
# ├───────┼───────┼───────┼───────┼───────┤
# | (0,3) | (1,3) | (2,3) | (3,3) | (4,3) |
# ├───────┼───────┼───────┼───────┼───────┤
# | (0,2) | (1,2) | (2,2) | (3,2) | (4,2) |
# ├───────┼───────┼───────┼───────┼───────┤
# | (0,1) | (1,1) | (2,1) | (3,1) | (4,1) |
# ├───────┼───────┼───────┼───────┼───────┤
# | (0,0) | (1,0) | (2,0) | (3,0) | (4,0) |
# └───────┴───────┴───────┴───────┴───────┘
#
# The characters list might looks like this:
#  snake = Snake([Position(1,2), Position(1,1), Position(2, 1)])
#  wall = Wall([
#    Position(0, 0), Position(1,0), Position(2, 0), Position(3, 0),
#    Position(4, 0), Position(4, 1), Position(4, 2), Position(4, 3),
#    Position(4, 4), Position(3, 4), Position(2, 4), Position(1, 4),
#    Position(0, 4), Position(0, 3), Position(0, 2), Position(0, 1),
#  ])
#  blank = Blank([
#    Position(1, 3), Position(2,3), Position(2,2), Postion(3,2),
#    Position(3,1)
#  ])
#  apple = Apple([Position(3,3)])
#  characters = Characters([snake, wall, blank, apple])

# Which visualizing each position in the game looks like this: 
# ┌───────┬───────┬───────┬───────┬───────┐
# | Wall  | Wall  | Wall  | Wall  | Wall  |
# ├───────┼───────┼───────┼───────┼───────┤
# | Wall  | Blank | Blank | Apple | Wall  |
# ├───────┼───────┼───────┼───────┼───────┤
# | Wall  | Sanke | Blank | Blank | Wall  |
# ├───────┼───────┼───────┼───────┼───────┤
# | Wall  | Snake | Snake | Blank | Wall  |
# ├───────┼───────┼───────┼───────┼───────┤
# | Wall  | Wall  | Wall  | Wall  | Wall  |
# └───────┴───────┴───────┴───────┴───────┘
#
# Or visualizing the characters looks like this:
# ┌───────────────────────────────────────┐
# | Wall                                  |
# |       ┌───────────────┬───────┐       |
# |       | Blank         | Apple |       |
# |       ├───────┐       └───────┤       |
# |       | Snake |               |       |
# |       |       └───────┐       |       |
# |       |               |       |       |
# |       └───────────────┴───────┘       |
# |                                       |
# └───────────────────────────────────────┘