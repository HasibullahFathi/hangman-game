# Hangman Game

Welcome to the Hangman Game!<br>
This is a classic word guessing game where you need to guess the word one letter at a time. The game has three difficulty levels: Easy, Medium, and Hard. Depending on the chosen difficulty level, different sets of words will be used.

![Responsice Mockup](/media/main-img.png)

## Game Overview
In Hangman, a player tries to guess a word chosen by the game. The word is represented by a series of underscores, with each underscore representing a letter in the word. The player guesses one letter at a time. If the guessed letter is in the word, all instances of that letter are revealed. If the guessed letter is not in the word, a part of the hangman diagram is drawn. The game continues until the player either guesses the word correctly or the hangman diagram is fully drawn (indicating the player has lost).

## Rules
Choose Difficulty Level: At the beginning of the game, you will be prompted to choose a difficulty level: Easy, Medium, or Hard. Each level has a different set of words.
Guess a Letter: You will be asked to guess a letter. If the letter is in the word, it will be revealed in its correct position(s). If the letter is not in the word, a part of the hangman will be drawn.
Win or Lose: The game ends when you either guess all the letters in the word correctly (win) or the hangman is fully drawn after 6 incorrect guesses (lose).
How to Play
Run the game script to start.
Choose a difficulty level when prompted.
Guess letters one at a time.
The game will provide feedback after each guess, showing the current state of the word and the number of misses.
Continue guessing until you either guess the word correctly or use up all your allowed misses.<br>
You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

## Features
- Choose the game level:
    - Get the user input to select the game level.
    - Select a word from the three separate word lists according to the specified game level.

- Visual Feedback:
    - The game uses ASCII art to visually represent the hangman.
    - The hangman diagram progresses with each incorrect guess, providing clear visual feedback on your progress.

- Input Validation and Error Handling:
    - Users cannot enter numbers or characters other than alphabetic letters.
    - Users must choose a valid game level to play the game.
    - Users must enter a single letter to guess the word.
    - To play again, users must enter 'Y' to continue or 'N' to exit.
    - All error messages are clear and guide the user for a better user experience.

- Color-Coded Messages:
    - The game uses 'colorama' for colored terminal text to make the game more engaging.
    - Different colors are used for prompts and results (e.g., red for errors, green for win messages).

- Clear Instructions:
    - Detailed instructions are provided at the beginning of the game, ensuring that new players understand how to play.
    - The rules and game flow are clearly explained.

- Replayability:
    - After the game ends, players are prompted to play again.
    - The console is cleared between game sessions for a fresh start each time.

- Progress Display:
    - The current state of the word is displayed after each guess, showing which letters have been correctly guessed and which positions remain unknown.

- Guess Tracking:
    - The game keeps track of all guesses, both correct and incorrect, and provides feedback on the number of misses.

- Win/Loss Feedback:
    - Clear messages are displayed when the player wins or loses, including the full word in case of a loss.

## Code Structure

The HangmanGame class encapsulates the state and behavior of a Hangman game session. Here's a concise summary of what it does:

- Initialization (__init__ method):

    - Initializes the game with attributes for difficulty level (self.level), the secret word to guess (self.word), a list of guessed letters (self.guesses), the number of incorrect guesses (self.misses), and the maximum allowed misses (self.max_misses).

- Choosing Game Level (choose_game_level method):

    - Prompts the player to choose a difficulty level (Easy, Medium, or Hard).
    - Validates the input to ensure it matches one of the predefined difficulty levels.
    - Returns a corresponding list of words based on the chosen difficulty level (EASY_WORDS, MEDIUM_WORDS, or HARD_WORDS).
- ascii_art.py: Contains the ASCII art for the hangman stages and the game logo.
- colorama: Used for colored terminal text.
- start_game(game, word_list): Initializes and starts the game loop.
- update_display(game): Updates and displays the current game state.
- check_guess(game, guess): Validates and processes each guessed letter.
- check_game_over(game): Checks if the game is over (win or lose) and handles end-of-game messages.
- clear_console(): Clears the console screen between game sessions for better readability.

## Testing
I have manually tested the App by doing the following:
- Passed the code through the PEP8 linter and confirmed there were no issues.
- Provided invalid inputs such as entering numbers where letters were expected, entering multiple letters when a single letter was expected, and entering incorrect input for levels and play-again prompts.
- Tested the App in my local terminal and the Code Institute Heroku terminal.

## Bugs
- To validate the guesses inside the try block, I used the (print) method instead of the (raise ValueError) method to show the error messages. Because of this, the guesses were incremented even if there were errors.

## Remaining bugs
- No bugs remaining.

## Validator Testing 
PEP8 testing
- No errors ware returned from PEP8online.com

## Deployment
The code was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
    - Prepare Python Application (requirements.txt: Lists the Python dependencies needed for application.)
    - Create Heroku App
    - Connect Heroku to GitHub
    - In the Heroku dashboard, go to the “Deploy” tab of the created app.
    - In the “Deployment method” section, click on "GitHub".
    - Authenticate and connect to GitHub account.
    - Search for the repository and click "Connect".
    - Deploy Application
    - In the Heroku dashboard, go to the “Settings” tab.
    - Click on “Reveal Config Vars” to add any environment variables the application needs in this app only set the PORT to 8000.
    - View  Application
    - Once the deployment is complete, click on “Open app” in the Heroku dashboard to view the live application.

## Credits
- Hangman logo used in App were taken from [ascii.co.uk](https://ascii.co.uk/) page.
- Hangman Stages used in App were taken from [Chris Horton](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) github page with a bit of modification.
- Code Institute for the deployment terminal