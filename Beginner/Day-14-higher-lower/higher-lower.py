import random
from art import logo, vs
from game_data import data
import os

print(logo)
first = random.choice(data)
second = random.choice(data)
while first == second:
  second = random.choice(data)

score = 0
over = False
while not over:

  print(
      f"Compare A: {first['name']}, {first['description']}, from {first['country']}"
  )
  print(vs)
  print(
      f"Compare B: {second['name']}, {second['description']}, from{second['country']}"
  )
  choice = input("Who has more followers: ").lower()

  if (choice == 'a' and first['follower_count']
      > second['follower_count']) or (choice == 'b' and first['follower_count']
                                      < second['follower_count']):
    score += 1
    if choice == 'a':
      first = first
    elif choice == 'b':
      first = second
    second = random.choice(data)
    while first == second:
      second = random.choice(data)
    os.system('clear')
    print(logo)
    print(f"Your right! Your score: {score}")

  else:
    over = True
    print(f"Sorry, that's wrong! Final score: {score}")
