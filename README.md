# Bulls And Cows

_No Spoilers, please! This is intended to be an exploration of the problem space: Please refrain from Googling. If you're already familiar with solutions, please try to "hint" rather than "solve" as the group explores the space._

_Likewise, please don't look in any folders with "spoiler_alert" in their names._

## Setup:

 1. Setup should happen automatically in GitPod - On you own computer, I recommeng using `pipenv` to manage development environments: You can run `pipenv install` to set everything up, and then `pipenv shell` to open a shell in the resulting environment. Alternately, you can run `pip install -r requirements.txt` to install the requirements (mostly, `pytest`) in your system Python _(this project assumes Python 3.8+)_

 2. You should now be able to run `pytest` in the top level folder, and see 8 passing tests.

 3. To try out the example Player, run `python main.py` to play 500 games and print out success statistics. This initial "random player" implementation works, but is... not great?

## The Game

Bulls and Cows is essentially a guessing game - The server picks a random Secret Code, and the Player tries to guess it, in as few guesses as possible.

Secret Codes are strings of four numerical digits, for example, "1234". In a normal game, Secret Codes cannot contain repeated digits, so "1111", "9000", and "7537" would not be valid. But they can include leading zeroes, for example, "0591".

The server provides feedback for your guess in the form of "Bulls and Cows", two integer values:

* The first integer value, referred to as "Bulls", is the number of digits that exactly match the secret code: A matching digit, in the same location. (for example, a guess that starts with "1" would earn one "Bull" if the secret code also started with "1".)

* The second integer value, "Cows", is the number of digits which do match the secret code, but are in the wrong position. For example, if your guess started with "1", but the secret code contained a "1" as the second digit, that would be worth one "Cow".

* Each digit can only earn one Bull, OR one Cow. Digits in your guess that do not appear at all in the Secret Code are not worth Bulls or Cows. For example, if you guess "1234" and the secret code is "5678", you will get 0 Bulls, and 0 Cows (no correct digits in the correct places, no correct digits in the wrong places). But if the secret code was "2134", that same guess would get 2 Bulls and 2 Cows (two correct digits in the correct spots, two correct digits in the wrong spots).

Once you guess the correct code, you win! Your "score" is based on the number of guesses it took you to find the Secret Code - fewer guesses is better.

(The amount of time or "work" you spend in producing each guess doesn't count, so anything you can do to make fewer, better guesses is worth it!)

## The Player

We will be implementing a Player class, with a few notable methods:

* **__init__(self)**: The constructor - sets up any initial state needed _(currently, none)_

* **guess()**: Returns a guess at the secret code _(currently, totally random)_

* **get_feedback(guess, bulls, cows)**: Receive "Bulls & Cows" style feedback about the Player's incorrect guesses _(currently, ignored)

The "Server" will run a series of games with your Player, following these steps:

   1. Start a new game, by generating a new Secret Code

   2. Instantiate a new Player instance (which invokes the `__init__()` method)

   3. Request a `guess()` from the Player

   4. Provide feedback for that guess via `get_feedback(guess, bulls, cows)`

   5. Repeat steps 3 & 4 until the Player guesses the Secret Code

The Server will also capture and display statistics about the minimum, maximum, and average number of guesses the Player needed to win, across a set of games (500 games by default).

## The Default "Random" Player

The default "Random" Player is very simple: It generates guesses completely at random, stores no state, and does not use the provided feedback. It is also _not very good_, in that it may require up to 80,000+ guesses to win a single game(?!), and often takes more than 11,000 guesses to win, on average.

## Why is this not good?

Given Secret Codes with 4 digits, there should be no more than 10,000 possible codes. In fact, there should be fewer, since our Secret Codes do not contain repeated digits. For example, the numerically highest possible Secret Code is 9876, the lowest possible code is 0123, and many other possible four-digit codes between them that contain repeated digits (1111, 1010, 1000, etc.) are also not allowed...

How can we improve this Player?

## Obvious fixes

Human players play Bulls and Cows using inference and intuition, which Computers are generally not very good at... But Computers can do repetitive, tedious tasks very quickly.

Our success criteria are to find the code with as few Guesses as possible - However, we can do as much calculation as we want before making each guess.

What can we do to make our guesses more valid? - In other words, wow can we avoid wasting guesses on invalid codes?

* We should never require more guesses than there are possible valid codes.

* On average, we should require fewer guesses than that. (How many valid Secret Codes are there? We should ideally not take more than half that number, on average...)

What can we do to make our guesses more accurate? More specifically, how can we use the Bulls and Cows feedback to make better guesses?

* The Bulls and Cows feedback tells us how similar our Guess is to the Secret Code, but it's not very specific. Without getting "too complicated", are there particular sets of Bulls and Cows feedback that are more actionable than others?

* 4 Bulls means we've guessed the code... What does it mean if we get 4 Cows?

* If we add our Bulls and Cows together into a "total score", what can that tell us? What is the maximum possible total score?

## Elementary, My Dear Watson

To quote fictional detective Sherlock Holmes:

> "When you have eliminated all that is impossible, then whatever remains,
however improbable, must be the truth."

Is it possible to apply Sherlock's style of deductive reasoning to this problem? How can we leverage the Bulls and Cows hints to "eliminate all that is impossible"?

How can a computer (which is better at tedious tasks than it is at analytical reasoning and intuition) to help us apply this wisdom?

