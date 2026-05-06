secret_num = 9
i = 0

while i < 3:
    guess = int(input("Guess num: "))

    if guess == secret_num:
        print("You win!")
        break

    i += 1
else:
    print("You failed")