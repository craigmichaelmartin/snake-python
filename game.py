import time

from game_builders.with_regular_walls import WithRegularWalls
from game_builders.with_portal_walls import WithPortalWalls
from database.operations import get_high_score, save_high_score

class Game():
  def __init__(self, graphics):
    # Save the `screen` instance that curses gave us
    self.graphics = graphics

    # Create an instance of the game builder we'll use,
    # and store it in `game_builder`
    # 🕵️ Try changing this to the `WithPortalWalls` builder
    self.game_builder = WithRegularWalls()

    # Setup the game
    self.setup_game()

  def setup_game(self):
    # Call `create` on the game builder and store the characters
    self.characters = self.game_builder.create()

    # Set the `game_over` to false
    self.game_over = False

    # Call the database operation to get the previous high score
    # and store it in `high_score`
    self.high_score = get_high_score()

    # Set a `delay` for the pause between turns
    self.delay = .2

  def start_game_loop(self):
    # This loop runs forever
    while True:
      
      # Respond to any user interactions
      key = self.graphics.get_key()
      self.handle_user_interactions(key)

      # If the game is not over, call `update` on each character
      # in case they have a "turn" (like how the snake moves forward)
      if not self.game_over:
        for character in self.characters.list:
          character.update(self)
      # Otherwise, save the score if its greater than the
      # existing high score
      else:
        # 🐛 BUG LOCATION 🐛
        # The high score is always being saved. However, we should 
        # only do the following two lines if `self.characters.score`
        # is greater than `self.high_score`
        self.high_score = self.characters.score
        save_high_score(self.high_score)

      # Ensure the game is still in a valid state
      self.ensure_valid_state()
      
      # Update the graphics to show what happened
      self.graphics.draw_game()
      
      # Since computers are so fast, we add a quick pause before
      # re-starting the loop for a new turn
      time.sleep(self.delay)

  def handle_user_interactions(self, key):
    # If the user presses the "q" key then quit the game
    if key == ord('q'):
      exit()

    # If the user presses the space key then re-setup the game
    if key == ord(' '):
      # 🐛 BUG LOCATION 🐛
      # We want the space bar to re-setup the game. There is a
      # method called `setup_game` but we are not calling it.
      # Instead we are calling `exit`.
      exit()

    # Pass whatever key is pressed to each character,
    # in case they are supposed to respond to it (like the arrow
    # keys for the snake).
    for character in self.characters.list:
      character.handle_user_interaction(key, self.graphics)

  @property
  def board_rows(self):
    return max(
      (pos for character in self.characters.list for pos in character.positions), 
      key=lambda pos: pos.x
    ).x + 1

  @property
  def board_columns(self):
    return max(
      (pos for character in self.characters.list for pos in character.positions), 
      key=lambda pos: pos.y
    ).y + 1

  def ensure_valid_state(self):
    all_positions = []
    for character in self.characters.list:
      for position in character.positions:
        all_positions.append(position)
    board_positions = self.board_rows * self.board_columns
    if len(all_positions) != board_positions:
      raise ValueError(
        f"Characters occupy {len(all_positions)} positions "
        f"but the board has {board_positions} positions."
      )
    if len(set(all_positions)) != len(all_positions):
      raise ValueError(
        "The same position is occupied more than once."
      )