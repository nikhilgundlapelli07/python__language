
import random

number = random.randint(1, 20)
attempts = 5

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 20")

for i in range(1, attempts + 1):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < number:
        print("Too low! Try a bigger number.")
    else:
        print("Too high! Try a smaller number.")

    print("Attempts left:", attempts - i)

else:
    print("Game Over!")
    print("Correct number was:", number)
