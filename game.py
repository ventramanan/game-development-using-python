import random

def guess_the_number():
    # Welcome message and random number generation
    print("Welcome to Guess the Number!")
    number = random.randint(1, 20)  # Generate a random number between 1 and 20
    attempts = 5  # Number of attempts allowed

    # Main game loop
    while attempts > 0:
        try:
            # User input with input validation
            user_guess = int(input("Enter the number between 1 to 20: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the user's guess is within the valid range
        if 1 <= user_guess <= 20:
            # Check if the user's guess is correct
            if user_guess == number:
                print("Congratulations, you won!")
                break
            # Provide feedback based on the user's guess
            elif user_guess < number:
                print("Your guess is low.")
            else:
                print("Your guess is high.")
            
            # Decrement the number of attempts
            attempts -= 1

            # Check if the user has used all attempts
            if attempts == 0:
                print("You have used all your turns. The correct number was:", number)
        else:
            # Prompt the user to enter a valid number within the specified range
            print("Please enter a number between 1 and 20.")

if __name__ == "__main__":
    # Start the game
    guess_the_number()

