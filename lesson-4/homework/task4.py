import random

def guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10
        print("Guess the number between 1 and 100!")
        while attempts > 0:
            guess = int(input("Your guess: "))
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("You guessed it right!")
                return
            attempts -= 1
            print(f"Attempts left: {attempts}")
        print("You lost. Want to play again?")
        response = input().lower()
        if response not in ['y', 'yes', 'ok']:
            break

guessing_game()
