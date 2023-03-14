import random
import string


class Player:

    def __init__(self):
        # Implement internal state here?
        self.last_returned_guess = 0
        self.available_digits = set(string.digits)

    def guess(self):
        """
        Guess four digits numbers, expressed as strings (e.g. "0146")
        (also: track any necessary state?)
        """
        # Generate a random number between 0 and 9,999
        # integer_guess = int(random.random() * 10000)
        # Convert to string
        # guess = str(integer_guess)
        # Right-justify with zeroes, e.g. "146" -> "0146"
        # padded_guess = guess.rjust(4, "0")
        # This is not a very good guess?
        # return padded_guess
        for n in range(self.last_returned_guess + 1, 10000):
            padded_guess = str(n).rjust(4, "0")
            padded_guess_chars = set(padded_guess)

            valid_chars = len(padded_guess_chars.intersection(
                self.available_digits)) == 4

            unique_chars = len(padded_guess_chars) == len(padded_guess)

            if valid_chars and unique_chars:
                self.last_returned_guess = n
                return padded_guess

    def get_feedback(self, guess, bulls, cows):
        """
        Act on feedback of "Bulls" (count of correct digits)
        and "Cows" (count of misplaced digits)
        B0, C0 => Totally wrong digits
        B4, C0 => (We won)
        B0, C4 => We have all the right digits, but totally wrong order...
        B+C=4  => We have all the right digits, some in right order...

        B1
        """
        if bulls == 0 and cows == 0:
            self.available_digits = (
                self.available_digits.difference(set(guess))
            )
                                    