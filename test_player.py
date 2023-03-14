from player import Player


def test_player_interface():
    # Make sure that the Player class has the expected interface
    p = Player()
    guess = p.guess()
    assert guess is not None
    assert isinstance(guess, str)
    assert len(guess) == 4
    bulls = 0
    cows = 0
    p.get_feedback(guess, bulls, cows)


# Possible improvement?
# def test_random_guesses_are_valid():
#     p = Player()
#     for i in range(100):
#         random_guess = p.random_guess()
#         assert is_valid_guess(random_guess)

# Valid Guesses:
#   Are Strings
#   Contain only numerical digits
#       (can have a leading 0!)
#   Have a length of 4, with no repeated digits

def test_guesses_are_strings():
    p = Player()
    guess = p.guess()
    assert isinstance(guess, str)


def test_guess_is_length_4():
    p = Player()
    guess = p.guess()
    assert len(guess) == 4


def test_guess_doesnt_repeat_digits():
    p = Player()
    guess = p.guess()
    assert len(set(guess)) == len(guess)


def test_first_guess_is_first_valid_number():
    p = Player()
    guess = p.guess()
    assert guess == "0123"


def test_second_guess_is_the_second_valid_number():
    p = Player()
    p.guess()
    second_guess = p.guess()
    assert second_guess == "0124"


def test_no_cattle_eliminates_digits():
    p = Player()
    assert len(p.available_digits) == 10
    p.get_feedback("0123", 0, 0)
    assert len(p.available_digits) == 6


def test_no_cattle_eliminates_first_guess():
    p = Player()
    p.get_feedback("0123", 0, 0)
    guess = p.guess()
    assert guess != "0123"

# possible strategy
# def test_b_plus_c_equals_4_locks_current_digits():


