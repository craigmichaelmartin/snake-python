def get_high_score():
  with open("database/high_score.txt") as file:
    return int(file.read())

def save_high_score(high_score):
  with open("database/high_score.txt", mode="w") as file:
    file.write(str(high_score))   