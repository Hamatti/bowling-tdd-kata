import doctest
import re
import sys
from itertools import pairwise

def pprint(*args):
  print(*args, file=sys.stderr)

def parse_bowling_input(input):
  players = []
  player_inputs = input.split('\n')
  for player in player_inputs:
    scores = [int(s) for s in re.findall('-?\d+', player)]
    if invalid_scores := [str(score) for score in scores if score < 0 or score > 10]:
        raise ValueError(f'{", ".join(invalid_scores)} is invalid score')
    if scores:
      name = player.split(str(scores[0]))[0].strip()
    else:
      name = player
    players.append((name, scores))
  return players

def bowling(input):
  """
  >>> bowling("Juhis 10")
  ('Juhis', 20)
  >>> bowling("Eve Stojbs 10")
  ('Eve Stojbs', 20)
  >>> bowling("Juhis 3 5")
  ('Juhis', 8)
  >>> bowling("Juhis 4 6")
  ('Juhis', 15)
  >>> bowling("Juhis 10 4 6 7 1\\nEve Stojbs 4 4 5 5 7 1")
  ('Juhis', 43)
  >>> bowling('Juhis 0 10 4 5')
  ('Juhis', 24)
  """
  winner = (None, -1)
  players = parse_bowling_input(input)
  for name, scores in players:
    pprint(name, scores)
    strikes = 0
    spares = 0
    first_throw = True
    frame_score = 0
    for score in scores:
      if first_throw:
        if score == 10:
          strikes += 1
        else:
          frame_score += score
          first_throw = False
      else:
        frame_score += score
        if frame_score == 10:
          spares += 1
        first_throw = True
        frame_score = 0

    pprint(strikes, spares)
    total_score = sum(scores) if scores else 0
    total_score += 10 * strikes + 5 * spares
    if total_score > winner[1]:
      winner = (name, total_score)
  return winner

if __name__ == '__main__':
  doctest.testmod()
  # with open('scores_2.txt', 'r') as score_file:
  #   print(bowling(score_file.read()))
  # example = "Yatas Del Lana 3 5 3 5 7 2 3 0 10 4 3\nEve Stojbs 3 7 3 3 9 1 6 4 2 3 1 0"
  # print(bowling(example))