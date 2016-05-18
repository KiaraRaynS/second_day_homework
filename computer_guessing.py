import random


def computer_guesses():
    game_mode = str(input('Mode: Easy or Hard? '))
    if game_mode.lower() == str('hard'):
        boundary_y = 100
        boundary_b = 100
    else:
        boundary_y = 10
        boundary_b = 10
    boundary_x = 1
    boundary_a = 1
    guesses_count = 0
    random_number = random.randint(boundary_x, boundary_y)
    while guesses_count < 5:
        computer_guess = random.randint(boundary_a, boundary_b)
        if computer_guess > random_number:
            print('Computer guess {} too large.'.format(computer_guess))
            print('Guesses remaining: '+ str(4 - guesses_count))
            guesses_count +=1
            if computer_guess == 1:
                boundary_b = 1
            else:
                boundary_b = int(computer_guess - 1)
        elif computer_guess < random_number:
            print('Computer guess {} too small.'.format(computer_guess))
            print('Guesses remaining: '+ str(4 - guesses_count))
            guesses_count +=1
            if computer_guess == 10:
                boundary_a = 10
            else:
                boundary_a = int(computer_guess + 1)
        elif computer_guess == random_number:
            print("The computer has correctly guessed the number: {}".format(random_number))
            break

run_question = str(input('Do you wish have computer play guessing game? Y/N '))
run_game = str('Y')
if run_question.upper() == run_game:
    computer_guesses()
