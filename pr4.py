import random 

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 attempts.")

while True:
    num = random.randint(1, 100)
    attempts = 1

    while attempts <= 7:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("enter a valid number between 1 and 100")
            continue

        guess_i = int(guess)

        if guess_i < 1 or guess_i > 100:
            print("enter a valid number between 1 and 100")
            continue

        if guess_i == num:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
        elif guess_i < num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        attempts += 1
        print(f"Attempts left: {7 - attempts + 1}\n")


    if attempts > 7 and guess_i != num:
        print(f"out of attempts the correct number is {num}")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
