import pytest
import inspect
from assignment import count_vowels, is_palindrome, remove_spaces, count_word_frequencies

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("input, expected", [
    ("Hello World", 3),
    ("Python Programming", 4),
    ("BCDFG", 0),
    ("AEIOUaeiou", 10),
    ("", 0)
])
def test1(input, expected):
    assert count_vowels(input) == expected
    assert check_contains_loop(count_vowels)

@pytest.mark.parametrize("input, expected", [
    ("madam", True),
    ("racecar", True),
    ("hello", False),
    ("Aibohphobia", True),
    ("", True)
])
def test2(input, expected):
    assert is_palindrome(input) == expected

@pytest.mark.parametrize("input, expected", [
    ("Hello World", "HelloWorld"),
    ("Python Programming Language", "PythonProgrammingLanguage"),
    ("  Remove   spaces  ", "Removespaces"),
    ("", ""),
    ("NoSpaces", "NoSpaces")
])
def test3(input, expected):
    assert remove_spaces(input) == expected

@pytest.mark.parametrize("input, expected", [
    ("hello hello world", {"hello": 2, "world": 1}),
    ("this is a test this is", {"this": 2, "is": 2, "a": 1, "test": 1}),
    ("count count count", {"count": 3}),
    ("", {}),
    ("word", {"word": 1})
])
def test4(input, expected):
    assert count_word_frequencies(input) == expected
    assert check_contains_loop(count_word_frequencies)
