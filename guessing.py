import random

easy_words = ['cat', 'dog', 'fish', 'bird', 'tree'] 
medium_words = ['python', 'jumble', 'garden', 'window', 'bottle']
hard_words = ['elephant', 'umbrella', 'diamond', 'computer', 'astronomy']    

print("Welcome to Guess The Word!")
print("Choose a difficulty level:") 
print("1. Easy")
print("2. Medium")      
print("3. Hard")
level = input("Enter 1, 2, or 3: ")
if level == '1':
    secret_word = random.choice(easy_words)
elif level == '2':
    secret_word = random.choice(medium_words)
elif level == '3':
    secret_word = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to Easy level.")
    secret_word = random.choice(easy_words) 

attempts = 0
print("Start guessing the word!")

while True:
    guess = input("Enter your guess: ")
    attempts += 1
    if guess.lower() == secret_word:
        print(f"Congratulations! You've guessed the word '{secret_word}' in {attempts} attempts.")
        break
    else:
        print("Incorrect guess. Try again!")

    hint=""
    for i in range(len(secret_word)):
        if i < len(guess) and guess[i].lower() == secret_word[i]:
            hint += secret_word[i]
        else:
            hint += "_"
    print(f"Hint: {hint}")

print("Thanks for playing Guess The Word!")            

11