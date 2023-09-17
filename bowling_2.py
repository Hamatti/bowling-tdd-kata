import doctest
import re
import sys
from itertools import pairwise

def get_frames(scores):
  return zip(scores[::2], scores[1::2])

def pprint(*args):
  print(*args, file=sys.stderr)

def parse_bowling_input(input):
  players = []
  player_inputs = input.split('\n')
  for player in player_inputs:
    frame_pattern = '(10|\d+ \d+)'
    frames = re.findall(frame_pattern, player)
    for i, frame in enumerate(frames):
      if frame == '10':
        frames[i] = '10 0'
    improved_scores = ' '.join(frames)
    scores = [int(s) for s in re.findall('-?\d+', improved_scores)]
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
  >>> bowling('Juhis')
  ('Juhis', 0)
  """
  winner = (None, -1)
  players = parse_bowling_input(input)
  for name, scores in players:
    strikes = 0
    spares = 0
    for first, second in get_frames(scores):
      if first == 10:
        strikes += 1
      elif first + second == 10:
        spares += 1

    total_score = sum(scores) if scores else 0
    total_score += 10 * strikes + 5 * spares
    if total_score > winner[1]:
      winner = (name, total_score)
  return winner

if __name__ == '__main__':
  doctest.testmod()
  with open('scores_2.txt', 'r') as score_file:
    print(bowling(score_file.read()))