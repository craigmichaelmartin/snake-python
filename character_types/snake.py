from character_types.character import Character
from position import Position


class Snake(Character):

  def __init__(self, positions):
    # The snake's body is stored in the `positions` list.
    # Important: it's head is the first element in the list and
    # its tail is the last element. This means that the position
    # the snake is moving into should be placed into the first
    # spot in this list, and when the snake moves the position
    # at the last spot in this list would be removed.
    self.positions = positions
    self.direction = 'right'
    self.color = 'white'

  @property
  def score(self):
    return len(self.positions) - 1

  @property
  def head_position(self):
    return self.positions[0]

  @property
  def tail_position(self):
    return self.positions[-1]

  def get_next_position(self):
    # If the snake is moving up it's next position is at
    # the same column and the row one above
    if self.direction == 'up':
      return Position(self.head_position.x, self.head_position.y + 1)

    # If the snake is moving down it's next position is at
    # the same column and the row one below
    if self.direction == 'down':
      return Position(self.head_position.x, self.head_position.y - 1)

    # If the snake is moving left it's next position is at
    # the column to the left and the same row
    if self.direction == 'left':
      return Position(self.head_position.x - 1, self.head_position.y)

    # If the snake is moving right it's next position is at
    # the column to the right and the same row
    if self.direction == 'right':
      return Position(self.head_position.x + 1, self.head_position.y)
      
    # Otherwise our direction value is invalid
    raise ValueError(f"{self.direction} is not a valid direction")
  
  def update(self, game):
    next_position = self.get_next_position()

    # Loop through all the characters and see if the snake's next
    # position is in their list of positions. For the character that
    # currently is occupying that position, call `hit_by_snake` on it
    for character in game.characters.list:
      if next_position in character.positions:
        character.hit_by_snake(game, next_position)
        
  def hit_by_snake(self, game, at_position):
    # If the snake would hit itself anywhere except it's tail
    # then the game is over.
    if at_position != self.tail_position:
      game.game_over = True

    # If the snake would hit its tail, this is actually fine
    # because when the snake moves its tail will no longer be there.
    # In this case, add the position to the snakes first position
    # (its head) and remove the snake's last position
    else:
      self.positions.insert(0, at_position)
      self.positions.pop()
  
  def handle_user_interaction(self, key, pygame):
    # If the up key is pressed and the snake is not going down
    # change the direction to up
    if key == pygame.K_UP and self.direction != 'down':
        self.direction = 'up'
      
    # If the down key is pressed and the snake is not going up
    # change the direction to down
    if key == pygame.K_DOWN and self.direction != 'up':
        self.direction = 'down'

    # If the left key is pressed and the snake is not going right
    # change the direction to left
    if key == pygame.K_LEFT and self.direction != 'right':
        self.direction = 'left'

    # 🐛 BUG LOCATION 🐛
    # Above we check if the up key, down key, or left key is pressed
    # and update the snake instance's `direction` accordingly.
    # However, we are not checking if the right key is pressed.
    # If it is, we should update `self.direction` to 'right'.
