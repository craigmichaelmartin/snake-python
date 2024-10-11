class Position:

  def __init__(self, x, y):
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