#Guessing game
secret_num = 5
guess_count = 0
while guess_count <= 2:
    guess = int(input("Guess: "))
    if guess == secret_num:
        print("You win!")
        break
    else:
        guess_count += 1
else: #This in unique, and very interesting. Reached at end of while loop, skipped with break
    print("Guess limit reached")