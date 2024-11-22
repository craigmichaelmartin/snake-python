from ui.curses.graphics import Graphics
from game import Game

# We use the curses engine due to the school's WiFi restricting ports
# that Replit's VNC server requires to run Pygame.
# If you are running this at home, comment-out line 1 and un-comment-out
# the line below this so that the game uses Pygame.
# from ui.pygame.engine import Engine


Graphics(Game)