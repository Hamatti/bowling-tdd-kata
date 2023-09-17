import doctest
import re
import sys

def parse_bowling_input(input):
  players = []
  player_inputs = input.split('\n')
  for player in player_inputs:
    print(player)
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
  ('Juhis', 10)
  >>> bowling("Eve Stojbs 10")
  ('Eve Stojbs', 10)
  >>> bowling("Juhis 10 7")
  ('Juhis', 17)
  >>> bowling("Juhis 10 7\\nEve Stojbs 6 5")
  ('Juhis', 17)
  >>> bowling("Juhis 0\\nEve Stojbs 8 9 10")
  ('Eve Stojbs', 27)
  >>> bowling("Eve Stojbs 6 5\\nJuhis 10 7")
  ('Juhis', 17)
  >>> bowling("Eve Stojbs 11")
  Traceback (most recent call last):
     ...
  ValueError: 11 is invalid score
  >>> bowling('Eve 2 -1 3')
  Traceback (most recent call last):
     ...
  ValueError: -1 is invalid score
  >>> bowling("Eve Stojbs")
  ('Eve Stojbs', 0)
  """
  winner = (None, -1)
  players = parse_bowling_input(input)
  for name, scores in players:
    total_score = sum(scores) if scores else 0
    if total_score > winner[1]:
      winner = (name, total_score)
  return winner

if __name__ == '__main__':
  doctest.testmod()
  with open('scores.txt', 'r') as score_file:
    print(bowling(score_file.read()))