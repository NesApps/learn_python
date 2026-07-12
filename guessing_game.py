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
    guess = int(input("Give your guess: "))
    if guess == secret_number:
        print("Congratulations, your guess is right")

    elif guess > secret_number:
        print("Too high")

    else:
        print("Too low")

    print("Thank you for playing")












