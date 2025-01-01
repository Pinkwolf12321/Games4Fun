import random
import time

# Welcome message
print("Welcome to Duck Duck Goose!")

# Get the number of players
num_players = int(input("Enter the number of players in the circle (including you): "))
players = [f"Player {i}" for i in range(1, num_players)] + ["You"]

# Game loop
while True:
    print("\nThe game begins!")
    time.sleep(1)

    # The 'ducker' moves around the circle
    for i, player in enumerate(players):
        if player == "You":
            action = input("Type 'Duck' or 'Goose': ").strip().lower()
            if action == "goose":
                print("You've chosen GOOSE! The chase is on!")
                print("You caught the computer! You're safe!")
                break
            elif action == "duck":
                print("Duck... moving to the next player.")
            else:
                print("Invalid choice. Type 'Duck' or 'Goose'.")
                continue
        else:
            # Computer decides
            action = random.choice(["Duck", "Goose"])
            print(f"{player} says {action}.")
            if action == "Goose":
                print(f"{player} chose GOOSE! You're being chased!")
                print("Run fast! You escaped safely!")
                break

    # Ask if the player wants to play again
    play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing Duck Duck Goose! Goodbye!")
        break

