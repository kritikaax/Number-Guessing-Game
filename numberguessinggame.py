import random

def numberGuessingGame():
    # Set the range for the number
    lowerBound = 1
    upperBound = 100
    # Randomly select a number
    secretNumber = random.randint(lowerBound, upperBound)
    attempts = 0
    guessed = False
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I have selected a number between {lowerBound} and {upperBound}. Can you guess it?")
    
    while not guessed:
        try:
            # Get the user's guess
            userGuess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if userGuess < lowerBound or userGuess > upperBound:
                print(f"Please guess a number within the range of {lowerBound} to {upperBound}.")
            elif userGuess < secretNumber:
                print("Too low! Try again.")
            elif userGuess > secretNumber:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secretNumber} in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Run the game
numberGuessingGame()