import random

random_number = random.randint(1,100)


def computer_guesses():
    game_mode = str(input('Mode: Easy or Hard? '))
    if game_mode == str('Hard'):
        x = 1
        y = 100
    else:
        x = 1
        y = 10
    guesses_count = 0
    while guesses_count < 5:
        computer_guess = random.randint(x,y)
        if computer_guess > random_number:
            print('Computer guess {} too large.'.format(computer_guess))
            print('Guesses remaining: '+ str(4 - guesses_count))
            y = computer_guess - 1
            guesses_count +=1
        elif computer_guess < random_number:
            print('Computer guess {} too small.'.format(computer_guess))
            print('Guesses remaining: '+ str(4 - guesses_count))
            x = computer_guess + 1
            guesses_count +=1
        elif computer_guess == random_number:
            print("The computer has correctly guessed the number: {}".format(random_number))
            break

run_question = str(input('Do you wish have computer play guessing game? Y/N '))
run_game = str('Y')
if run_question == run_game:
    computer_guesses()