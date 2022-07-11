import random


class Player:

    def __init__(self):
        # Implement internal state here
        self.state = None

    def guess(self):
        # Generate a random number between 0 and 9,999
        integer_guess = int(random.random() * 10000)
        # Convert to string
        guess = str(integer_guess)
        # Right-justify with zeroes, e.g. "146" -> "0146"
        padded_guess = guess.rjust(4, "0")
        return padded_guess

    def get_feedback(self, guess, bulls, cows):
        # TODO: Do something with bulls, cows feedback?
        pass
