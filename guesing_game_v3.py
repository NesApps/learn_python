import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed correctly in {attempts} attempts!")
        break

    elif guess > secret_number:
        print("📈 Too high! Try again.")

    else:
        print("📉 Too low! Try again.")

print("Thank you for playing")