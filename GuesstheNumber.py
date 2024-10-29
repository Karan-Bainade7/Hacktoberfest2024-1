import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        # Ask the player to enter their guess
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
    
if __name__ == "__main__":
    guess_the_number()
