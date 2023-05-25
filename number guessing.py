import random

def number_guessing_game():
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    name = str(input("Enter your name:"))
    print(f"I am thinking of a number from 1 to 100. Can you   guess it {name}...")
    
    while True:
        n= random.randint(1, 100)
        attempts = 0
        
        while attempts < 10:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == n:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                print("BRAVO!! You're the winner...")
                break
            elif guess < n:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        if attempts == 10:
            print(f"Game Over! You reached the maximum number of attempts. The secret number was {n}.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

number_guessing_game()
