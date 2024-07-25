# Team Name Hangman Game

![opening](https://github.com/user-attachments/assets/2d1b2fd4-3e52-4e15-b1d1-6f7e5c8b3d9c)

Team Name Game is a Pyhton terminal game to test player' knowledge on the teams in the "big four" North American sports leagues. These contain: Major League Baseball (MLB), National Basketball Association (NBA), National Football League (NFL), and National Hockey league (NHL).
The player must try to guess the team name that is chosen at random and is penalised every time they choose an incorrect letter. If the player manages to correctly guess all the letters, they have won the game. Should their guess be incorrect, they will gradually be adding to a built-in hangman diagram and after 5 incorrect gueses the diagram will be complete and they will have been unsuccessfl in winning the game.

The deployed version of this game can be accessed [here](https://team-name-hangman-game-f7bfa00d8815.herokuapp.com/)

## User Experience (UX)

### Site Purpose

The purpose of this site is to provide the user a simple hangman game that challenges the user to complete a team name letter-by-letter. Once the game has been completed, the user can decide to restart the game and play agian.


### Intended Audience

The site is for anyone who has an interest in the main North American sports leagues. it will also allow the user who wishes to pass some time and keep themselves busy while offering a challenge fo their knowledge on the teams form the four major sports leagues in the USA and Canada.

### Communication

The game informs the user from the opening page, through a clear hangman diagram, that this will be a hangman style game. It will also let the player know when they have performed various tasks. These include: guessing a correct letter, choosing incorrectly, entering an invalid value e.g. a number or symbol, when they have successfully c ompleted the game , and if they have failed to guess the word. The user will also be asked upon completion of the game whether they wish to try agian.

### Future Improvements

* The implementation of a leaderboard and high score facility.
* Aesthetic improvements as the game, in its current state, can appear quite basic. These include: a wider colour range, an ASCII heading and images for various stages of the game.
* More leagues and teams could be added to allow for a wider range of words to choose at random.
* The option for the user to choose what word, by number of letters, they would like to choose prior to making their first letter selection.
* The ability to select which league and have the answers be from that league only so that the options available would be more focused on the user's choice of league.

## Features

### Opening Screen

* At the beginning the game the user is asked if they wouuld like to play and how many attempts they have before the hangman is complete and they have been unsuccessful in their attempt.

![opening](https://github.com/user-attachments/assets/b238a5e5-1db1-4d68-8cd1-6f6d13d8c9ea)

### Correct Selection

* The user will be clearly informed when theya re successful in choosing a correct letter. The hangman diagram has been designed to remain the same should the user be correct.

  ![correct-guess](https://github.com/user-attachments/assets/df1ffef4-850b-4d41-ad5a-ceda94711db1)

### Incorrect Guess

* The diagram of the hangman will be updated to reflect the fact that the user has chosen a letter that is not contained within the word. They will also be informed in text that the letter they have chosen is not correct and to select another letter.

  ![incorrect-guess](https://github.com/user-attachments/assets/1bbc8bbf-d6b4-4a3a-8af2-d25ecc770635)

### Invalid Selection

* The player will be visually notified if they attempt to enter an invalid character into the game. Invalid characters are any character that do not satisfy the alphabetic only (inalpha) function included.

![invalid-guess](https://github.com/user-attachments/assets/6b973cf4-3be8-42f3-a00f-af06203f950c)

### Successful Completion

* When they full word is correctly guessed, the screen will reflect this. The user will aslo be congratulated and asked if they wish to play the game again.

  ![all-correct-guesses](https://github.com/user-attachments/assets/06b7c7d3-ef62-4863-a64b-aa820f6acaa0)

### Unsuccessful Completion

* when the user is unsuccessful in completing the game, a completed hangman will appear alongside a message informing that they have been unsuccessful and asking if they wish to try agian and wishing them luck in their next attempt
  
  ![all-incorrect](https://github.com/user-attachments/assets/453a13e7-3f4f-40fd-9fb4-1adbe579e2c9)

## Flowchart

![Hangman Lucid Chart](https://github.com/user-attachments/assets/0882030d-65f2-4b48-be24-2cd9124a1cdb)

## Validation Testing

* I tested my code through two seperate validators:

* I sued Code Institute Python Linter (available [here](https://pep8ci.herokuapp.com/#) for both the run adn teams python pages. Both pages successfully passed with no errors.

A screenshot of the run page validation can be found below here.

![run-page-validation](https://github.com/user-attachments/assets/947df624-fd7f-4060-80dd-ff1b71ed3cf7)

The screenshot of the teams page validation can be found below here.

![teams-page-validation](https://github.com/user-attachments/assets/a922b956-0721-46fc-8441-ccd3db639a74)







