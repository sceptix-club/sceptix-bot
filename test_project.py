from helpers import get_rps, get_rpssl, play_rps, play_rpssl
from pytest import raises

def test_get_rps():
    assert get_rps("rock") == "Rock"
    assert get_rps("R") == "Rock"
    assert get_rps("sci  ") == "Scissors"
    assert get_rps("s") == "Scissors"
    assert get_rps("  PAPER") == "Paper"
    with raises(Exception):
        get_rps("Tone")
        get_rps("Lizzards")


def test_get_rpssl():
    assert get_rpssl("rock") == 0
    assert get_rpssl("R") == 0
    assert get_rpssl("sci  ") == 2
    assert get_rpssl("Scissors") == 2
    assert get_rpssl("  PAPER") == 1
    assert get_rpssl("sp") == 3
    assert get_rpssl("L") == 4
    assert get_rpssl("lizzy") == 4
    with raises(Exception):
        get_rpssl("Stone")
        get_rpssl("Bike")
        get_rpssl("David")


def test_play_rps():
    assert play_rps("Rock", "Scissors") == "You Won!"
    assert play_rps("Paper", "Rock") == "You Won!"
    assert play_rps("Scissors", "Paper") == "You Won!"
    assert play_rps("Rock", "Rock") == "That's a tie!"
    assert play_rps("Paper", "Scissors") == "You lost \U0001F641"
    assert play_rps("Scissors", "Rock") == "You lost \U0001F641"
    assert play_rps("Rock", "Paper") == "You lost \U0001F641"
