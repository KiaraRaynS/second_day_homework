import random


def computer_guesses():
    game_mode = str(input('Mode: Easy or Hard? '))
    if game_mode.lower() == str('hard'):
        x = 1
        y = 100
        a = 1
        b = 100
    else:
        x = 1
        y = 10
        a = 1
        b = 10
    guesses_count = 0
    random_number = random.randint(x, y)
    while guesses_count < 5:
        computer_guess = random.randint(a, b)
        if computer_guess > random_number:
            print('Computer guess {} too large.'.format(computer_guess))
            print('Guesses remaining: '+ str(4 - guesses_count))
            guesses_count +=1
            if computer_guess == 1:
                b = 1
            else:
                b = int(computer_guess - 1)
        elif computer_guess < random_number:
            print('Computer guess {} too small.'.format(computer_guess))
            print('Guesses remaining: '+ str(4 - guesses_count))
            guesses_count +=1
            if computer_guess == 10:
                a = 10
            else:
                a = int(computer_guess + 1)
        elif computer_guess == random_number:
            print("The computer has correctly guessed the number: {}".format(random_number))
            break

run_question = str(input('Do you wish have computer play guessing game? Y/N '))
run_game = str('Y')
if run_question.upper() == run_game:
    computer_guesses()
