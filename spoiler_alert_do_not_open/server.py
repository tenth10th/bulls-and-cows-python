import random
import string
import sys

DEFAULT_TARGET_GAMES = 500


def runBullsAndCowsPlayer(PlayerClass, target_games=None):
    if (not target_games):
        target_games = DEFAULT_TARGET_GAMES
    total_guesses = 0
    total_games = 0
    min_guesses = None
    max_guesses = None

    print(f"Playing {target_games:,d} games...")
    old_percent_done = 0
    while (total_games < target_games):
        player = PlayerClass()
        bulls = 0
        cows = 0
        guesses = 0
        secret_code = generate_code()
        while bulls < 4:
            guesses += 1
            guess = player.guess()
            if not guess:
                print(f"Disqualified: Got a falsey guess: {guess}")
                sys.exit(1)

            if not isinstance(guess, str):
                print(f"Disqualified: Got a non-string guess: {guess}")

            if len(guess) != 4:
                print(f"Disqualified: Expected length 4, got a Guess of length {len(guess)}: {guess}")
                sys.exit(1)

            bulls, cows = score_code(secret_code, guess)
            player.get_feedback(guess, bulls, cows)

        total_guesses += guesses
        total_games += 1

        if (min_guesses is None) or (guesses < min_guesses):
            min_guesses = guesses

        if (max_guesses is None) or (guesses > max_guesses):
            max_guesses = guesses

        new_percent_done = round((total_games / target_games) * 100)
        if new_percent_done != old_percent_done:
            print(f"   {format(new_percent_done)}%    ", end='\r')
        old_percent_done = new_percent_done

    average_guesses = round(total_guesses / total_games, 2)
    print(f"Won in an average of {int(average_guesses):,d} guesses per game!")
    print()
    print(f"   Minimum Guesses: {min_guesses:,d}")
    print(f"   Maximum Guesses: {max_guesses:,d}")
    print(f"       Total Games: {total_games:,d}")
    print(f"     Total Guesses: {total_guesses:,d}")
    print()


def generate_code():
    # Produce a unique list of digits
    digits = list(string.digits)
    # Shuffle it
    random.shuffle(digits)
    # Return the first 4 digits (as a string)
    return ''.join(digits[0:4])


def score_code(guess, code):
    # Return (bulls, cows) feedback for a guess, vs. a secret code
    bulls = 0
    cows = 0
    unique_digits = list()

    for i, digit in enumerate(guess):
        if i >= len(code):
            continue
        if code[i] == digit:
            bulls += 1
        elif digit in code and digit not in unique_digits:
            cows += 1
            unique_digits.append(digit)

    return bulls, cows

