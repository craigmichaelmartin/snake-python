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