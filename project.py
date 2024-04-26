import random
from pyfiglet import Figlet
import time

# Create word lists for different levels
easy = [
    "building",
    "computer",
    "astronaut",
    "programming",
    "upset",
    "rescue",
    "safety",
    "meaningful",
    "queue",
    "caring",
    "creative",
    "patient",
    "headline",
    "planet",
    "picture",
    "escape",
    "concert",
    "lawyer",
    "calm",
    "understanding",
    "experience",
    "entertain",
    "flu",
    "dolphin",
    "actress",
    "actor",
    "attentive",
    "architect",
    "pilot",
    "dangerous",
    "model",
    "fashion",
    "reporter",
    "interview",
    "training",
    "important",
    "spin",
    "experience",
    "slippery",
    "split",
    "pretend",
    "entertain",
    "audience",
]
middle = [
    "earthquake",
    "typhoon",
    "drought",
    "rich",
    "poor",
    "healthy",
    "sick",
    "strong",
    "weak",
    "wet",
    "dry",
    "village",
    "clean",
    "dirty",
    "bright",
    "dark",
    "expensive",
]
hard = [
    "delight",
    "diligent",
    "cunning",
    "dim",
    "arrogant",
    "organic",
    "diary",
    "leisure",
]


def main():
    print(
        "Welcome to guess the word! Which mode would you like to play?\nModes:\n1. Easy\n2. Middle\n3. Hard"
    )

    while True:
        mode = input("Select Mode (1/2/3): ")
        if mode in ["1", "2", "3"]:
            selected_word = modes(mode)
            try:

                # Mark game start
                figlet = Figlet()
                fonts = figlet.getFonts()
                figlet.setFont(font=random.choice(fonts))
                print(figlet.renderText("Game Start"))

                # Game logic
                guessed = set()
                trials = len(selected_word) + 3
                playing = True
                start_time = time.time()

                # Play until all letters are found or max number of tries is reached
                while playing and trials > 0:
                    display_word(selected_word, guessed)
                    try:
                        guess = guess_word(guessed)
                    except KeyboardInterrupt:
                        print("\nGame ended due to keyboard interrupt.")
                        break

                    # Add correct letter to guessed
                    if guess in selected_word:
                        guessed.add(guess)

                        # Terminate the game if the player guesses the word
                        if set(selected_word).issubset(guessed):
                            playing = False
                            end_game(selected_word, guessed, start_time)

                    # Decrement trials if guessed wrong letter
                    else:
                        trials -= 1
                        print(f"Incorrect! You have {trials} attempts left.")

                # Count the total
                if playing:
                    end_game(selected_word, guessed, start_time)

                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again != "yes":
                    break
            except KeyboardInterrupt:
                print("\nGame ended due to keyboard interrupt.")
                break
        else:
            print("Please enter a valid mode (1, 2, or 3).")


# Randomly generate a word according to the selected mode
def modes(mode):
    if mode == "1":
        return random.choice(easy)
    elif mode == "2":
        return random.choice(middle)
    elif mode == "3":
        return random.choice(hard)


# Display the word with guessed letters filled in
def display_word(word, guessed):
    for char in word:
        if char in guessed:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()


# Validate the entered letter
def guess_word(guessed):
    while True:
        letter = input("Guess a letter: ").lower()

        if not letter.isalpha() or len(letter) != 1:
            print("Please enter a single letter.")
        elif letter in guessed:
            print("You have already guessed that letter.")
        else:
            return letter


# End the game and display the result
def end_game(word, guessed, start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    display_word(word, set(word))  # Display the complete word
    print(f"Total time spent: {elapsed_time:.1f} seconds")
    print(
        f"Congratulations! You guessed the word: {word}"
        if set(word).issubset(guessed)
        else f"Game over! The word was: {word}"
    )


if __name__ == "__main__":
    main()
