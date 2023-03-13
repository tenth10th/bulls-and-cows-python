from server import score_code, generate_code
import pytest

REPEATEDLY = 100


@pytest.mark.parametrize("guess, code, expected_bulls, expected_cows", [
    ("1234", "1234", 4, 0),
    ("1234", "4321", 0, 4),
    ("1234", "5678", 0, 0),
    ("1234", "1932", 2, 1),
    ("4221", "2342", 0, 2),
    ("", "1234", 0, 0),
    ("1234567890", "5678", 0, 0),
])
def test_score_code(guess, code, expected_bulls, expected_cows):
    assert score_code(guess, code) == (expected_bulls, expected_cows)


def test_generate_code():
    for i in range(0, REPEATEDLY):
        code = generate_code()
        assert code is not None
        assert isinstance(code, str)
        assert len(code) == 4
        assert len(code) == len(set(code))
