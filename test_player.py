from player import Player

def test_player():
    # Make sure that the Player class has the expected interface
    p = Player()
    guess = p.guess()
    assert guess is not None
    assert isinstance(guess, str)
    assert len(guess) == 4
    bulls = 0
    cows = 0
    p.get_feedback(guess, bulls, cows)

