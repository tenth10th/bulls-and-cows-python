from itertools import combinations, permutations
import string

# Combination: A set of options (in no particular order)

# Permutation: A specific ordered sequence of the items in a set


class Player:

    def __init__(self):
        # Implement internal state here
        self.guesses = []
        self.combination_mode = True
        self.combinations = [
            ''.join(combo) for combo in combinations(string.digits, 4)
        ]
        for x in range(0, 10_000):
            guess = str(x)
            padded_guess = guess.rjust(4, "0")
            add_guess = True
            for i in range(0, 3):
                if padded_guess[i] in padded_guess[i+1:]:            
                    add_guess = False
            if add_guess:
                self.guesses.append(padded_guess)

    def guess(self):
        if self.combination_mode:
            return self.combinations.pop()
        
        return self.guesses.pop()

    def get_feedback(self, guess, bulls, cows):

        """
        First, iterate through all Combinations
            Until we hit (0, 0) or 4 Total?
        """

        if (bulls, cows) == (0, 0):
            bad_digits = set(guess)
            # get rid of bad options?
            good_guesses = list()
            for guess in self.guesses:
                guess_set = set(guess)
                if not bad_digits.intersection(guess_set):
                    good_guesses.append(guess)
            self.guesses = good_guesses
            self.combination_mode = False
        if bulls + cows == 4 and len(self.guesses) > 24:
            # We have the right numbers! But not in the right spots?
            good_digits = list(guess)
            # Let's just try every possible order of these digits
            all_permutations = permutations(good_digits, 4)
            # And turn them back into strings (guesses)
            self.guesses = [''.join(guess) for guess in all_permutations]
            self.combination_mode = False


if __name__ == "__main__":
    p = Player()
    print(f"{len(p.guesses)} Guesses:", p.guesses)
