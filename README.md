# 100 Days of Code - The Complete Python Pro Bootcamp (2023) on Udemy

My solutions & other work for the projects included in the [Python Pro Bootcamp 2023 by Dr. Angela Yu](https://www.udemy.com/course/100-days-of-code/).

## Day 1 - Beginner - Working with variables in Python to manage data

* [Project: Cover Band name generator](/Day-001/.)

## Day 2 - Beginner - Understanding data types and how to manipulate strings

* [Project: Tip Calculator](/Day-002/.)

## Day 003 - Beginner - Control flow and logical operators

* [Project: Treasure Island](/Day-003/.)

## Day 004 - Beginner - Randomization and Python lists

* [Coding challenge work and project: Rock, Paper, Scissors!](/Day-004/.)

## Day 005 - Beginner - Python loops

* [Project: Random password generator](/Day-005/.)

## Day 006 - Beginner - Python functions & Karel (really Reeborg) the robot

* [Coding challenge work and project: Reeborg's maze](/Day-006/.)
* Note: My solution (reeborgs-world-maze-redux.py) works for all three problem
    samples and was 25/25 on random worlds.  That said I do not know if it would
    work for larger/more complex worlds as it uses the build_wall() function.
    The instructor's solution was definitely simpler and has been included as well.

## Day 007 - Beginner - Hangman

* [Project: Hangman](/Day-007/.)
* Note: There are a couple of features I want to add to this version:
  * Use a bigger dictionary
  * Display a list of letters already guessed (right, wrong or both?)
  * Don't subtract a life if they guess a letter already guessed.  I thought that was already in the instructor's TODO but it doesn't appear to be.

## Day 008 - Beginner - Function parameters & Caesar cipher

* [Project: Caesar cipher](/Day-008/)
* Note: My solution re-prompts the user for valid responses.  In particular I did not use the modulus (%) function to fix invalid shift input.

## Day 009 - Beginner - Dictionaries, nesting and the Secret Auction

* [Project: The Secret auction](/Day-009/.)
* Note: Written as specified it will cheerfully overwrite a bidder with the same name

## Day 010 - Beginner - Functions with outputs

* [Project: Calculator](/Day-010/.)
* Note: my solution includes code to exit cleanly from the calculator, in order to avoid this:

![Recursion!][def]

[def]: /images/recursion_image.png

## Day 011 - Beginner - The Blackjack capstone project

* [Capstone project 1: Blackjack](/Day-011/.)
* Note: My solution handles Blackjacks differently from the instructor's, but I think it works well.  I also did not move scoring to a separate function.

## Day 012 - Beginner - Scope & number guessing game

* [Project: Guess the number game](/Day-012/.)
* Note: My understanding of general code design is to minimize the number of global variables, which should be named using uppercase letters and not modified.  Try to put variables that will be modified in functions if possible.
* Note: Try to adopt the use of global variables declared at the top of the file as a way to adjust settings without having to change the code.  Depending on the project, it might be better to move them to a separate config / credentials file.

## Day 013 - Beginner - Debugging - How to find and fix errors in your code

* No project in this lesson, just interactive coding exercises on Auditorium
* Troubleshooting principles, most of which I already use but sometimes a reminder is good:
  * Describe the problem
  * Reproduce the bug
  * Play computer and evaluate each line
  * Fix the errors and watch for red underlines
  * Print is your BFF!
  * Use a debugger
    * Resource: <https://pythontutor.com/visualize.html#mode=edit>
    * Set breakpoints to see how many times the line is executed
  * Take a break!
  * Ask a friend - not your friend print(). They won't make the same assumptions you have - fresh eyes.
  * Run the code often
  * Ask StackOverflow (The Oracle?)
    * Resource: <https://stackoverflow.com/questions/tagged/python>
  * Be sensitive to how code looks.  The more code you read, the better you get at debugging.
* My 3 favorite Dr. Yu quotes in this lesson:
  * "You know you've become a professional developer when you create really big bugs."
  * "If Hollywood movies portray hackers as typing away, that is not the truth. Most of the time we are debugging, we are staring deep into space and trying to figure out what it is that we've written that is causing this catastrophic failure of our code."
  * "Failure is your friend."

## Day 014 - Beginner - Higher Lower game project

* [Project: The Higher Lower game](/Day-014/.)
  * Minimal instruction provided for this project, only the ASCII art and data dictionary.
  * This was challenging but it helped me to absorb some of the previous lessons, in particular variable scope and creating a recursive function.  The main body of code contains just 4 lines.
  * I also used my friend Brian Whitley's suggestion about DEBUG statements.  Namely, declare DEBUG as a global variable (True/False) and wrap debugging print statements in an if statement to print them (or not) as needed.

## Day 015 - Intermediate - Setup local development environment & coffee machine project

* [Project: The Coffee machine](/Day-015/.)
* The coffee machine - with a nod to [H2G2](https://hitchhikers.fandom.com/wiki/Sirius_Cybernetics_Corporation)
* This was a challenging but fun project.  I had some issues updating a global variable within a function and had to work it out by doing some research, along with some trial & error.

### Coffee machine redux

* I was not happy with the way my code came out, so I decided to try again.  Much happier with the second version.  Lessons learned:
  * Don't forget what you already know (an old one)
  * When in doubt, grab the entire list. It makes extracting what you want easier.
* My revised version also has the following features:
  * A better menu item display
  * More resources! (for better testing)
  * A **lot** of DEBUGGING statements, easily enabled/disabled via the global DEBUG
  * Functions to dynamically generate the menu list and items on the order input line.  This automatically picks up additions to the MENU dictionary with no code changes.

## Day 016 - Intermediate - Object Oriented Programming (OOP)

* [Project: The Coffee machine in OOP](/Day-016/.)
* The classes were provided, with the goal of learning how to use them.  I understood the concept but struggled a bit with the implementation.  RTFD a bit more thoroughly.
* Since the provides classes did a lot of the heavy lifting, the code written was fairly short
* My version does a couple of extra things:
  * Lists the drink cost, formatted in currency ($0.00)
  * Checks for an invalid selection and re-prompts

## Day 017 - Intermediate - The Quiz project & the benefits of OOP

* [Project: The Quiz game in OOP](/Day-017/.)
* Still having trouble putting the concept into code, but getting there.
* The final version of the code uses questions from [Open Trivia Database](https://opentdb.com/)
  * Code changes were minimal, two variable names in main.py were adjusted to reflect the new data structure
  * Some cleanup of the API data was necessary for formatting to look correct, in particular removal of '&quot;'

## Day 018 - Intermediate - Turtle & the Graphical User Interface (GUI)

* [Coding work: Timmy the turtle draws a dashed line, shapes and goes on a random walkabout](/Day-018/coding-work/.)
  * Timmy got limbered up during the coding work, even if he did wander off the map sometimes while out for a random walkabout.
* [Project: Timmy the turtle draws Hirst dots](/Day-018/project/.)
  * Now that Timmy's an artist maybe he will make millions!  Then I can retire and take more Udemy classes.
  * I came up with a completely different solution to this project:
    * I used the setworldcoordinates() method to set the home coordinates (0, 0) in the lower left of the screen instead of the middle
    * Then I used two nested for loops to set the x & y coordinates and teleport() to move Timmy
    * I don't know if this would be problematic on a different screen size, I'd have to check

## Day 019 - Intermediate - Instances, state and higher order functions

* [Coding work: Etch-A-Sketch with Timmy the Turtle](/Day-019/coding-work/.)
* [Project: Timmy the Turtle goes racing](/Day-019/project/.)
  * Timmy and his buddies go racing at Roy G. Biv Speedway!  Can you guess the winner?
  * This project created multiple instances of the Turtle class for the raceway.  All the turtle objects were placed in a list for easy looping.
  * My final version includes a couple of extras:
    * Set the window title
    * The winning turtle does a burnout in the middle of the screen
    * The winning turtle is announced on the screen
    * A break condition to prevent multiple winners

## Day 020 & 021 - Intermediate - Animation, coordinates, inheritance and slicing

* [Project: Build the classic Snake Game!](/Day-020+021/project/.)
  * No need to dig out that old Nokia phone, you can build & play the snake game in Python
  * My version generates random color snake segments
  * Things to work on incorporating into my programming:
    * Write some code for testing, then move it to functions or methods as needed
    * Separate things into smaller functions / methods for easier re-use.  Refactoring is your friend!
    * "Use the CONSTANTS, Luke" (my phrase) to tweak settings without having to dig into the code

## Day 022 - Intermediate - Build Pong, the famous arcade game

* [Project: Build Pong, OOP style](/Day-022/.)
  * This project definitely tested my OOP skills.  My bounce solution was more difficult than it needed to be.  Reworked the code after watching her solution.  Some things to keep in mind:
    * Pay a bit more attention to the goal in each section.  Doing so might have kept me from making the bounce code needlessly complicated
    * Try not to overthink things!
  * My solution has the following extra features:
    * Speed the ball up after each contact with a paddle
    * Dashed center line
    * Game over / winner condition

## Day 023 - Intermediate - The Turtle Crossing capstone project

* [Capstone project 2: Turtle Crossing](/Day-023/.)
  * After struggling with the Pong project, this one went really well.  Hopefully that means I was able to absorb the lessons learned during my difficulties.

## Day 024 - Intermediate - Files, directories and paths

* [Project: Mail merge](/Day-024/.)
  * Introduction to absolute and relative paths, reading and writing files
  * Updated the snake game to save the high score to a file so it can be reread the next time the program runs
  * Created a simple mail merge program, my version does the following:
    * Only reads the starting_letter.txt file once
    * Replaces Angela's name with Zane's!

## Day 025 - Intermediate - Working with CSV data and the Pandas library

* [Project: U. S. States map quiz](/Day-025/.)
* Lots of coding work and examples in this lesson:
  * Opening a CSV file using the CSV module vs Pandas
  * Working with CSV data using column labels
  * Creating a Python dictionary & turning it into a Pandas dataframe
  * Writing to CSV files
  * Central Park (NYC) Squirrel Census!
    * My solution creates a list of non-blank, unique colors from the source data so they don't have to be known beforehand
  * I feel like I could use a lot more experience with Pandas, still struggling with the syntax a bit
* My favorite Dr. Yu quote in this lesson:
  * "So much faff..." (in reference to code required for reading CSV with the built-in csv module versus Pandas)
  * Faff (plural faffs) (Britain, Ireland, Australia, New Zealand, slang): An overcomplicated task, especially one perceived as a waste of time.

## Day 026 - Intermediate - List comprehension and the NATO alphabet

* [Project: The NATO alphabet](/Day-026/.)
  * List and dictionary comprehension is very powerful, if a bit terse at first.  Feels like I have a pretty good handle on it, although for some reason I did make the very last statement more complicated than it necessary.  It worked but the output what not quite as expected.  I was able to fix it after reviewing the lessons and thinking a bit more.
  * The U. S. States map quiz was also updated to use list comprehension to create the states to be learned CSV file
