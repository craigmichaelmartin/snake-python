import time
import pygame

from game_builders.with_regular_walls import WithRegularWalls
from game_builders.with_portal_walls import WithPortalWalls
from database.operations import get_high_score, save_high_score
from ui.graphics import Graphics

class Game():
  def __init__(self):
    # Create an instance of the game builder we'll use,
    # and store it in `game_builder`
    # 🕵️ Try changing this to the `WithPortalWalls` builder
    self.game_builder = WithRegularWalls()

    # Setup the game
    self.setup_game()

    # Start the game
    self.start_game_loop()

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
    # Create a Graphics instance passing it this game instance
    graphics = Graphics(self)

    # This loop runs forever
    while True:
      
      # Respond to any user interactions
      self.handle_user_interactions()

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

      # Update the graphics to show what happened
      graphics.draw_game()
      
      # Since computers are so fast, we add a quick pause before
      # re-starting the loop for a new turn
      time.sleep(self.delay)

  def handle_user_interactions(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        # If the user presses the escape key then exit the program
        if event.key == pygame.K_ESCAPE:
          exit()
        # If the user presses the space key then re-setup the game
        if event.key == pygame.K_SPACE:
          # 🐛 BUG LOCATION 🐛
          # We want the space bar to re-setup the game. There is a
          # method called `setup_game` but we are not calling it.
          # Instead we are calling `exit`.
          exit()
          
        # Pass whatever key is pressed to each character,
        # in case they are supposed to respond to it (like the arrow
        # keys for the snake).
        for character in self.characters.list:
          character.handle_user_interaction(event.key, pygame)

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