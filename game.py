import time
import pygame

from game_builders.with_regular_walls import WithRegularWalls
from game_builders.with_portal_walls import WithPortalWalls
from database.operations import get_high_score, save_high_score
from ui.graphics import Graphics

class Game():
  def __init__(self):

    self.game_builder = WithRegularWalls()

    self.board, self.characters = self.game_builder.create()
    self.game_over = False
    self.high_score = get_high_score()
    self.delay = .2

    self.graphics = Graphics(self)

    while True:
      self.handle_user_interactions()
      self.score = self.characters.score()
      if self.game_over:
        if self.score > self.high_score:
          self.high_score = self.score
          save_high_score(self.high_score)
      else:
        for character in self.characters.list:
          character.update(self)

      self.graphics.draw_game()
      # computers are fast, simulate the world's slowness
      time.sleep(self.delay)

  def handle_user_interactions(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          exit()
        elif event.key == pygame.K_SPACE:
          (self.board, self.characters) = self.game_builder.create()
          self.game_over = False
        else:
          for character in self.characters.list:
            character.handle_user_interaction(event.key, pygame)