rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
rps = [rock, paper, scissors]
rps_s = ["rock", "paper", "scissors"]
opp_input = random.randint(0,2)
if user_choice >= 3 or user_choice < 0:
    print("Please enter a valid number.")
else:
    print(f"You chose {rps_s[user_choice]}.")
    print(rps[user_choice])
    print(f"Computer chose {rps_s[opp_input]}.")
    print(rps[opp_input])
    if user_choice == opp_input:
        print("It's a draw.")
    elif user_choice == 0 and opp_input == 2:
        print("You win.")
    elif user_choice == 1 and opp_input == 0:
        print("You win.")
    elif user_choice == 2 and opp_input == 1:
        print("You win.")
    else:
        print("You lose.")
    
    


                  
