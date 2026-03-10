#!/usr/bin/python3
"""Returns tuple of length and first character of a string."""


def multiple_returns(sentence):
    """Return (length, first_char) or (0, None) if empty."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])

