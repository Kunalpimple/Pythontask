import random
secret_number = random.randint(1, 100) # Generate a random number between 1 and 100
# Keep asking the user to guess until they get it right
while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")
