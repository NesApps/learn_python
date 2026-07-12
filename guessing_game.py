# secret_number = 7
#
# while True:
#     guess = int(input("Give me your guess: "))
#
#     if guess == secret_number:
#         print("congratulation, your guess is right")
#
#     elif guess > secret_number:
#             print("Number too high")
#
#     else:
#         print("Number too low")




secret_number = 7

while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("🎉 Congratulations! You guessed correctly!")
        break
    elif guess > secret_number:
        print("📈 Too high! Try again.")

    else:
        print("📉 Too low! Try again.")

print("Thank you for playing")












