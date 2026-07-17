import random

def get_secret_number():
    secret_number = random.randint(1, 10)
    return secret_number
def get_guess():
    guess = int(input("Enter your guess: "))
    return guess
def check_guess(guess, secret_number):
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed correctly")
        return True
    elif guess > secret_number:
        print(f"📉 Too high! Try again.")
        return False
    else:
        print(f"📈 Too low! Try again.")
        return False

def play_game():
