
'''Create an interactive guessing game.  The program should ask for a users name,
pick a random number between 1-100, give the user hints if they guess wrong,
and congratulate the user before exiting the program if a user guesses correctly'''


import random


def guessing_game():
    user_name = raw_input("hello.  Welcome to my game.  What should I call you?")
    num = random.randint(1, 100)
    print(num)
    print("Hello %s! Lets play!" % user_name)
    while True:
        guess = int(raw_input("I'm thinking of a number between 1 and 100.  What do you think it is?  "))
        print(guess)
        if guess == num:
            print("THAT'S CORRECT!!! :)")
            break
        elif guess > num:
            print("That number is too high.  Guess again")
        elif guess < num:
            print("That is too low.  Guess again")
        else:
            print("That is not a valid input.  Try again")


if __name__ == '__main__':
    guessing_game()
