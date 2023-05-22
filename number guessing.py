import random
def number_guessing_game():
  n = random.randint(1, 100)
  print("WELCOME TO THE NUMBER GUESSING GAME!")
  name = str(input("Enter your name:"))
  print(f"I am thinking of a number from 1 to 100. Can you guess it {name}...")
  attempts = 0
  while attempts < 10:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == n:
      print(
        f"CONGRATULATIONS {name}!! You have guessed it Right in {attempts} attempts!"
      )
      print("Bravo!! You're the WINNER.")
      print("PLAY AGAIN?")
      break
    elif guess < n:
      print("Your guess is Too LOW! Try again.")
    else:
      print("Your guess is Too High!, Try again.")
      if attempts == 10:
        print(
          f"Game Over! You have reached the maximum number of attempts. The Guessed Number was {n}."
        )
        print("PLAY AGAIN?")
number_guessing_game()
