
import pytest
import spellcheck


alpha = "Checking the length & structure of the sentence."
#beta = "This sentence should fail the test"

@pytest.fixture
def input_value():
    input = alpha
    return input

def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars."""
    """
    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    assert spellcheck.char_count(input_value) < 50

    assert spellcheck.word_count(input_value) < 10

    # raise NotImplementedError()


def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period."""
    """
    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value) == '.'

    # raise NotImplementedError()
