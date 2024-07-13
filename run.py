import random
import ascii_art


STAGES = ascii_art.stages

EASY_WORDS = [
    "apple", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "ink", "jug",
    "kite", "lamp", "moon", "nest", "owl", "pen", "queen", "rat", "sun", "tree"
]

MEDIUM_WORDS = [
    "grape", "lemon", "tiger", "chair", "piano", "zebra", "wheat", "train", "plane", "beach",
    "camel", "flute", "globe", "horse", "knife", "monkey", "peach", "robot", "shark", "torch"
]

HARD_WORDS = [
    "elephant", "computer", "astronaut", "microwave", "television", "saxophone", "kaleidoscope", "encyclopedia", "hippopotamus", "chrysanthemum",
    "binoculars", "circumference", "constellation", "laboratory", "thermometer", "university", "vocabulary", "xylophone", "yesterday", "zoologist"
]

class HangmanGame:
    """
    HangmanGame class to represent the Hangman game.
    """

    def __init__(self):
        """
        Initialize the Hangman game.
        """
        self.level = ""
        self.word = ""
        self.guesses = []
        self.misses = 0
        self.max_misses = 6

    def choose_game_level(self):
        """
        Prompt the player to choose the difficulty level of the game and return the corresponding word list.
        
        Returns:
            list: A list of words corresponding to the chosen difficulty level.

        while : validates that the player is typing the level correctly to choose the difficulty level.
        """
        while True:
            self.level = input("Choose one of the difficulty levels: Easy, Medium or Hard: ").lower()
            if self.level == "easy":
                return EASY_WORDS
            elif self.level == "medium":
                return medium_WORDS
            elif self.level == "hard":
                return  HARD_WORDS
            else:
                print(f'Invalid level {self.level}. Please choose Easy, Medium or Hard.')


def check_guess(game, guess):
    """
    Check the player's guessed letter, update the game state, and handle invalid inputs with error messages.
    
    Args:
        game (HangmanGame): The game instance.
        guess (str): The letter guessed by the player. 
    """

    try:
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
        
        if guess in game.guesses:
            print(f"You've already guessed {guess} letter.")
        
        game.guesses.append(guess)

        if guess not in game.word:
            game.misses += 1

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def start_game(game, word_list):
    """
    Start the Hangman game with the given word list and manage the game loop.

    Args:
        game (HangmanGame): The game instance.
        word_list (list): The list of words to choose from based on the selected difficulty level.
    """
    game.word = random.choice(word_list).upper()
    game.guesses = []
    game.misses = 0

    check_guess(game, input("Guess a letter: ").upper())

    print(game.word)
    print(game.guesses)

    print(STAGES[game.misses])
    print(f"Misses: {game.misses}")


game = HangmanGame()
start_game(game, EASY_WORDS)


        
