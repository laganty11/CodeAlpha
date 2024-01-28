import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts_left = max_attempts

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts_left -= 1
                print(f"Attempts left: {attempts_left}")
                if attempts_left == 0:
                    print("Game over! You ran out of attempts. The word was:", word_to_guess)
                    break
            word_display = display_word(word_to_guess, guessed_letters)
            print(word_display)

            if "_" not in word_display:
                print("Congratulations! You guessed the word:", word_to_guess)
                break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
