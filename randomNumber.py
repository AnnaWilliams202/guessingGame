import random

num = random.randint(1,100)
max_attempts = 10
attempt = 0

print("Welcome to Random Number Game")
print("I have selected the number between 1 and 100")
print(f"You have {max_attempts} attempts to guess correct number ")

for i in range(max_attempts):
    guess = int(input("Guess a number between 1 and 100: "))
    attempt += 1
    if guess > num:
        print("Too high. Try again!")
    elif guess < num:
        print("Too low. Try again!")
    else:
        print(f"Congratulation! You have guessed {guess} from {attempt} attempts")
        break
else:
    print(f"Sorry you have not guessed the correct number. You used all {max_attempts} attempts. "
          f"Correct number was {num} ")

