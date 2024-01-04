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
* Note: My solution re-prompts the user for valid responsese.  In particular I did not use the modulus (%) function to fix invalid shift input.

## Day 009 - Beginner - Dictionaries, nesting and the Secret Auction

* [Project: The Secret auction](/Day-009/.)
* Note: Written as specified it will cheerfully overwrite a bidder with the same name

## Day 010 - Beginner - Functions with outputs

* [Project: Calculator](/Day-010/.)
* Note: my solution includes code to exit cleanly from the calulator, in order to avoid this:

![Recursion!][def]

[def]: /images/recursion_image.png

## Day 011 - Beginner - The Blackjack capstone project

* [Capstone project 1: Blackjack](/Day-011/.)
* Note: My solution handles Blackjacks differently fron the instructor's, but I think it works well.  I also did not move scoring to a separate function.

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
