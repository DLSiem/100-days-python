#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

target = 33


def choose_level():
    level = input("Choose difficulty. Type 'easy' or 'hard'. ").strip()
    print(level != 'easy')
    if level == 'easy' or level == 'hard':
        return level
    else:
        print("Enter valid difficulty!")
        return choose_level()


def guess():
    gues = int(input('Make a guess: '))
    if gues > 100 or guess < 1:
        print("Number not in range.")
        return guess()
    return gues


def play(attempts):
    total_attempts = attempts
    print(f"You have {attempts} remaining to guess the number.")
    stop = False
    while not stop:

        attempts -= 1
        hei = guess()
        if hei == target:
            print("You win!")
            print(f"You did it in {total_attempts-attempts} attempts.")
            print(f"You have {attempts} remaining.")
            break
        elif hei > target:
            print("Too high.")
            print(f"You have {attempts} remaining.")
        elif hei < target:
            print("Too low.")
            print(f"You have {attempts} remaining.")
        if attempts == 0:
            print("You lose!")
            stop = True


no_of_guesses = 0
print("Welcome to the Number Guessing Game!")
stop = False
while not stop:
    print("I'm thinking of a number between 1 and 100 both inclusive.")
    difficulty = choose_level()
    if difficulty == 'easy':
        no_of_guesses = 10
    else:
        no_of_guesses = 5
    play(no_of_guesses)
    another_game = input(
        "You want to play another game? type 'y' or 'n'. ").strip()
    if another_game == 'n':
        stop = True
