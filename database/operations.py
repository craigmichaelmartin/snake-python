def save_high_score(high_score):
  # We save the high score in a file
  with open("database/high_score.txt", mode="w") as file:
    file.write(str(high_score))   

def get_high_score():
  # We read the high score from a file
  with open("database/high_score.txt") as file:
    return int(file.read())