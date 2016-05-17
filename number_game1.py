import random


def number_game():
    game_level = input('Easy or Hard mode? ')
    if game_level == 'Hard':
        random_number = random.randint(1, 100)
        possible_value = "1 - 100"
    else:
        random_number = random.randint(1, 10)
        possible_value = "1 - 10"
    guesses = 0
    while guesses < 4:
        user_guess = int(input('Guess a number between: {} '.format(possible_value)))
        if user_guess == random_number:
            print('Congratulations! You guessed the number! ' + str(random_number))
        elif user_guess > random_number:
            print('Sorry, that number is too high.')
            guesses += 1
            print('Guesses left: ' + str(4 - guesses))
        elif user_guess < random_number:
            print('Sorry, that number is too low.')
            guesses += 1
            print('Guesses left: ' + str(4 - guesses))


user_answer = str(input('Would you like to play number game? Y/N '))
repeat_game = str('Y')
if user_answer == repeat_game:
    number_game()
else:
    print('Have a good day!')
