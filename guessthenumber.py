import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of attempts
attempts = 0

# Start the game
while True:
    # Get the player's guess
    guess = input("Guess a number between 1 and 100 please...: ")
    
    # Convert guess to a number
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number.")
        continue
    
    # Increase attempt count
    attempts += 1

    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts!")
        break
