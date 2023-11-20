import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 20)
    attempts = 5

    while attempts > 0:
        user_guess = int(input("Enter the number between 1 to 20: "))
        
        if user_guess == number:
            print("Congratulations, you won!")
            break
        elif user_guess < number:
            print("Your guess is low.")
        else:
            print("Your guess is high.")
        
        attempts -= 1

        if attempts == 0:
            print("You have used all your turns. The correct number was:", number)

if __name__ == "__main__":
    guess_the_number()
