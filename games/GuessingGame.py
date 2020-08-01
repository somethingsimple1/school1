import time
import random
import string




def welcome(): #welcoming the user in to the game 3

    ask_name = 'placeholder'
    global name
    print('Welcome to my guessing game.')
   




    while ask_name != ('yes', 'no'):
        try:
            name = input('What do you want your name to be? : ')
            ask_name = input('Do you want "{}" to be your name. yes or no : '.format(name))
            ask_name = str(ask_name)
            ask_name = ask_name.lower()
            ask_name = ask_name.strip()

            if ask_name == "yes":
                pick_levels()

            elif ask_name == 'no':
                pass


        except ValueError:
            print('That is not option. Please try something else.')
            print('')




def pick_levels():
    level = "placeholder"

    global max #the max number
    global int_random # the random number

    while level != ('easy', 'medium', 'hard'):  # using the wihle loop so the code stays here untill it is meet
        try:  # try to try the code and if something worng it gose to except and prints and error then loops

            print('')
            print('Hello {}'.format(name))
            print('what level do you want?')
            level = input('easy, medium, hard or 1, 2, 3: ')
            print('')

            level = str(level)
            level = level.lower()
            level = level.strip()

            if level == 'hard' or level == '3':  # hard level
                print('level is going to be hard')  # saying what level it is
                print('')
                int_random = random.randint(1, 1000)  # the random number
                max = 1000  # max number
                main_code() #jumps to the main code

            elif level == 'medium' or level == '2':
                print('level is going to be medium')
                print('')
                int_random = random.randint(1, 500)
                max = 500
                main_code()

            elif level == 'easy' or level == '1':
                print('level is going to be easy')
                print('')
                int_random = random.randint(1, 100)
                max = 100
                main_code()

            else:
                print('That is not option. Plaese try something else.')
                print('')

        except ValueError: # if it finds somethig worng with the code upbove it goes here and tells me the somthing is worng / didn't work and loops
            print('That is not option. Please try something else.')


def main_code(): #the game

    amount_guess = 0  # the anount to times it took to guess the number
    guess = "placeholder" # the guess that the user is giving
    guess_list = [] # the list to print out the guess they took


    while int_random != guess:  # it will stay in this loop untill int_randdom is equal to there guess
        try:
            int_guess = input("Enter an integer from 1 to {}: ".format(max))

            guess_list.append(int_guess) #adds the nuber to the list
            guess = int(int_guess)  # test if it's a sting float or a int

            if guess > max or guess < 1 : #so the user cant go above the max number
                print('That number is not between 1 and {}'.format(max))
                print("")
                guess_list.pop()

            elif guess > int_random:
                amount_guess = amount_guess + 1
                print("Guess is high")
                print("")


            elif guess < int_random:
                amount_guess = amount_guess + 1
                print('Guess is to low')
                print("")

            else:
                amount_guess = amount_guess + 1

                print("")
                print("------------------------------------------")
                print("you guessed it!")
                print("It took you {} guess to gess the number and these where your guess.".format(amount_guess)) #tells the user how meany guess they took
                print(', '.join(guess_list))#tells the number they put down as their guess.
                print("------------------------------------------")

                guess_list.clear()#to clear the list for the next round
                play_again()

          # if it's a sting for a float it will go here and loop
        except ValueError:
            print('That is not a number. that is a world or a float')
            print("")
            guess_list.pop() #


def play_again(): #ask the user if they want to play again
        ask_play = "placeholder"

        while ask_play != ('yes', 'no'):
            try:
                ask_play = input('Do you want to play again {}? yes or no : '.format(name))
                ask_play = str(ask_play)
                ask_play = ask_play.lower()

                if ask_play == 'yes':
                    pick_levels()

                elif ask_play == 'no':
                    exit()

            except ValueError:
                print('That is not an option. Plaese try somethig else.')
                print('')




welcome() #takes the user to the start of the program