class Board:

  def __init__(self, rows, columns, block_size, block_gap, border):
    self.rows = rows
    self.columns = columns
    self.block_size = block_size
    self.block_gap = block_gap
    self.border = border

  @property
  def width(self):
    return self.columns *\
      (self.block_size + self.block_gap) +\
      (self.border * 2)

  @property
  def height(self):
    return self.rows *\
      (self.block_size + self.block_gap) +\
      (self.border * 2)
    
  @property
  def size(self):
    return (self.width, self.height)