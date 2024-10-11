# Snake

Welcome to snake! It works pretty well, but there are some bugs and some opportunities to make it better!

## Fix Bugs
1. The apple is the same color as the walls. That is confusing. Update the apple's color to be different (and change any other colors to make it look nice)
2. The high score is incorrectly updated after every game, regardless of whether it is actually higher than the previous high score.
3. The apple should start in a random location, but I hardcoded it to always start at Position(3,3).


## New feature ideas
1. Add Slow, Medium, and Fast modes. If the user presses "s" for slow the delay is .5 seconds, if they press "m" for medium the delay is .2 seconds, and if they press "f" for fast the delay is .1 seconds.
2. Add a Pause option. If the user presses "p" for pause, the game pauses.
3. Allow the game to be restarted by pressing the space bar.
1. Allow the user to choose different versions of the game by pressing "1" for the standard version, "2" for the version with portal walls.
2. Add a `bomb` character that appears in a random location and "explodes" (effecting each square touching it) after a random amount of turns. If the snake head hits the bomb or explosion the game ends. After an explosion the bomb is removed for a random ammount of turns and then appears again. Add a `with_bombs` game builder for this.