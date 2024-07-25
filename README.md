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

* I also used [Extends Class](https://extendsclass.com/python-tester.html) Python syntax validator to ensure the syntax on both my pages were correct.

  The run page passed without any syntax errors. The screenshot can be found below here.

![python-validator](https://github.com/user-attachments/assets/a0a9fb1a-78d0-41d6-b30a-672d5afc54cd)

  The teams page also passed without any syntax errors. The screenshot can be found below here.

![teams-syntax-validator](https://github.com/user-attachments/assets/5973a002-5090-48ec-84b1-4434ac63ff31)

## Bugs

* I originally wanted to choose minus symbols instead of underscores but I found that this would result in the space alloted for the chosen word being elongated unnecessarily.

* I attempted to use the inalnum method instead of the inalpha option as two team names contain numbers (49ers & 76ers) but this made the game respond incorrectly. I remedied this by 
  changing the respective team names to letters only (niners & sixers) which are sometimes substituted informally for each team.

## Unfixed Bugs

* On Heroku the underscores can appear as one long continual line which can obscure the number of letters contained in each word. I tried various alternatives like asterisks and hash marks but these changes caused the game to give the full word whether or not the chosen letter was correct or not. The best option was to use the underscore as it created less issues than the other alternatives.

## Creation

  * I used Github and Github Codespaces to complete the code for botht the teams page, which contains all the words that can be presented to the user, annd the run page whic contains   
    the code necessary to allow the page to function and the game to begin and run successfully.
    
## Deployment

### Version control

* Github and Github codespace were used to ente the contents of both run and teams pages contained within.

* Git commands were used to allow changes to be made through the commit process. The commit process involves three steps which are outlined below:

  * git add . : This tells the system that there is to be a commit committed in the system.
  * git commit -m "" : This command contains the content that will appear in the commits of the Github repository and allows for the tracking of changes made.
  * git push : Pushes the committed change to the repository and must be executed before changes made to pages can be saved.

### Page Deployment

* Deployment through Heroku was completed using the following steps.
  
  * I created a Heroku account and added my card details.
    
  * I created my app as Team-Name-Hangman-Game as that was the best option available at the time and chose the region of Europe.
    
  * Go to settings and change necessary buildpacks (node.js and python) and add config_vars (port-8000).
    
  * Choose deploy and select Github to link your code to Heroku.
    
  * Allow automatic deployment as this allows site to be constantly online.
    
  * The app must be deployed through the main branch which links to the template created for project 3.
    
  * Wait for the deployment to complete and when "Your app was successfully deployed" appears on screen click the "view" button underneath to see your app in a new tab.
    
  * click "Run Program" to begin the code and allow the user to see the opening screen.

## Content

### Technologies Used

  * The app was written using the Python language.
  * The following code content was used:
    * random: To allow the word chosen to be completed to be a random selection.
    * inalpha: This function allowed the options chosen by the user to be restricted to letters only and resulted in an on-screen error message if the user chose either a number or a         symbol.
    * else if : This statement allows for  
   
  * Github was used to create both py pages used in this app.
  * LucidChart [Lucid Chart](https://lucid.app/documents#?folder_id=home) was used to create the flow chart.
  * CI Python Linter [Python Linter](https://pep8ci.herokuapp.com/#) and [Extends Class](https://extendsclass.com/python-tester.html) were used to validate both the code and syntax.

## Credits

I would like to thank my facilitator, my mentor and my classmates for their help throughout the creation of this app.

I used [Net Ninja](https://www.youtube.com/watch?v=Ozrduu2W9B8&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK) for some of the basic python coding.
 
I also used both [QuickRef](https://quickref.me/python) and [Codedex](https://www.codedex.io/) for additional help.


