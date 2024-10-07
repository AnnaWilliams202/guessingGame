import random

words = ["python", "java", "swift", "javascript", "ruby"]
word = random.choice(words)

max_attempts = 3
attempts = 0

print('Wellcome to guessing game')
print("I picked a word from programming languages")
print (f'You have {max_attempts} attempts to guess the word ')

for i in range(max_attempts):
    guess = input("Enter your guess: ").lower()
    attempts += 1
    if len(guess) < len(word):
        print("Sorry your word is too short. Try again! ")
    if len(guess) > len(word):
        print("Sorry your word is too long Try again! ")
    elif (len(guess)==len(word)) & (guess != word):
        print("Sorry your guess is incorrect, but length is correct.  Try again! ")
    else:
        print(f"Congratulation! You guessed the word correctly from {attempts} attempts!")
        break
else:
    print(f"Sorry you used all {attempts} attempts. Correct word was {word} ")