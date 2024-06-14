#Step 1
import random
import data

word_list = data.words_list
logo = data.logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

wrong_attempts = 0
stages = data.stages
str_stages = ["_" for i in range(len(chosen_word))]

print(logo)


while wrong_attempts < len(stages):
    print(f"{' '.join(str_stages)}\n")

    user_guess = input("Guess a letter: ").lower()
    if user_guess in str_stages:
        print(f"You've already guessed {user_guess}")
        print('----------------------------------\n')

    if user_guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == user_guess:
                str_stages[i] = user_guess
                print(" ".join(str_stages))
                print(data.stages[len(stages) - wrong_attempts - 1])
                print("-----------------------------------\n")
    else:
        wrong_attempts += 1
        print("You guessed " + user_guess +
              ", that's not in the word. You lose a life.")
        
        print(data.stages[len(stages) - wrong_attempts - 1])
        print('--------------------------------\n')
        if wrong_attempts == len(stages):
          print('You lose')
          break 
    if "_" not in str_stages:
        print("You win.")
        break
    
