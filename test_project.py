import pytest
from unittest.mock import patch
from project import modes, display_word, guess_word, end_game, easy, middle, hard


def test_modes(monkeypatch):
    # Test selecting mode 1 (easy)
    assert modes("1") in easy

    # Test selecting mode 2 (middle)
    assert modes("2") in middle

    # Test selecting mode 3 (hard)
    assert modes("3") in hard

    # Test selecting an invalid mode
    assert modes("h") == None


# test display_word
@pytest.mark.parametrize(
    "word, guessed, expected_output",
    [
        ("hello", {"h", "e", "l", "o"}, "h e l l o"),
        ("hello", {"h", "e"}, "h e _ _ _"),
        ("hello", set(), "_ _ _ _ _"),
    ],
)
def test_display_word(capsys, word, guessed, expected_output):
    display_word(word, guessed)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output

'''
# test guess_word
@pytest.mark.parametrize(
    "input_text, guessed, expected_output, expected_message",
    [
        ("a", set(), "a", ""),
        ("123", set(), "1", "Please enter a single letter."),
        ("a", {"a"}, "a", "You have already guessed that letter."),
    ],
)
def test_guess_word(
    capsys, monkeypatch, input_text, guessed, expected_output, expected_message
):
    monkeypatch.setattr("builtins.input", lambda _: input_text)
    guessed_letter = guess_word(guessed)
    captured = capsys.readouterr()
    assert guessed_letter == expected_output
    assert expected_message in captured.out'''


# test end_game
@pytest.mark.parametrize(
    "word, guessed, start_time, expected_message",
    [
        (
            "hello",
            {"h", "e", "l", "o"},
            0,
            "Congratulations! You guessed the word: hello",
        ),
        ("hello", {"h", "e", "l"}, 0, "Game over! The word was: hello"),
    ],
)
def test_end_game(capsys, word, guessed, start_time, expected_message):
    end_game(word, guessed, start_time)
    captured = capsys.readouterr()
    assert "Total time spent:" in captured.out
    assert expected_message in captured.out


if __name__ == "__main__":
    pytest.main()
