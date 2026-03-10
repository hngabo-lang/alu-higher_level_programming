#!/usr/bin/python3
"""Returns a tuple with length and first char of a string."""


def multiple_returns(sentence):
    """Return (length, first_char) tuple, or (0, None) if empty."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
