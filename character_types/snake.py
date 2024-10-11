from character_types.character import Character
from utilities.position import Position


class Snake(Character):

  def __init__(self, positions):
    self.positions = positions
    self.direction = 'right'
    self.color = 'white'

  def get_next_position(self):
    if self.direction == 'up':
      return Position(self.head_position.x, self.head_position.y - 1)
    elif self.direction == 'down':
      return Position(self.head_position.x, self.head_position.y + 1)
    elif self.direction == 'left':
      return Position(self.head_position.x - 1, self.head_position.y) 
    elif self.direction == 'right':
      return Position(self.head_position.x + 1, self.head_position.y)
    else:
      raise ValueError(f"{self.direction} is not a valid direction")
  
  def update(self, game):
    new_position = self.get_next_position()

    for character in game.characters.list:
      if new_position in character.positions:
        character.hit_by_snake(game, new_position)
        
  def hit_by_snake(self, game, at_position):
    if at_position != self.tail_position:
      game.game_over = True
    else:
      self.positions.insert(0, at_position)
      self.positions.pop()
      
  def score(self):
    return len(self.positions) - 1
  
  def handle_user_interaction(self, key, pygame):
    if key == pygame.K_UP and self.direction != 'down':
        self.direction = 'up'
    elif key == pygame.K_DOWN and self.direction != 'up':
        self.direction = 'down'
    elif key == pygame.K_LEFT and self.direction != 'right':
        self.direction = 'left'
    elif key == pygame.K_RIGHT and self.direction != 'left':
        self.direction = 'right'

  @property
  def head_position(self):
    return self.positions[0]

  @property
  def tail_position(self):
    return self.positions[-1]