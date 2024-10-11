from abc import ABC


# This is the base class that all world builders extend.
class GameBuilder(ABC):

  def create(self):
    raise ValueError("Must implement 'create'")