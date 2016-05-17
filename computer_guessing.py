import random

random_number = random.randint(1,100)


def computer_guesses():
    guesses_count = 0
    while guesses_count < 4:
        computer_guess = random.randint(1,100)
        if computer_guess > random_number:
            print('Computer guess {} too large.'.format(computer_guess))
            print('Guesses remaining: '+ str(4 - guesses_count))
            guesses_count +=1
        elif computer_guess < random_number:
            print('Computer guess {} too small.'.format(computer_guess))
            print('Guesses remaining: '+ str(4 - guesses_count))
            guesses_count +=1
        elif computer_guess == random_number:
            print("The computer has correctly guessed the number: {}".format(random_number))

run_question = str(input('Do you wish have computer play guessing game? Y/N '))
run_game = str('Y')
if run_question == run_game:
    computer_guesses()