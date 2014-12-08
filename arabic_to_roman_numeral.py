def _arabic_to_additive_roman_numeral(arabic):
    pass


def _apply_subtractive_rule(purely_additive_roman):
    pass


def arabic_to_roman_numeral(arabic):
    """Convert an arabic numeral to a roman numeral.

    This roman numral is of the standard form utilizing substractive notation
    as defined in the following wiki article as to increase compactness:

        http://en.wikipedia.org/wiki/Roman_numerals#Reading_Roman_numerals.


    Args:
        arabic (string): An arabic numeral.

    Returns:
        string.
    """
    purely_additive_roman = _arabic_to_additive_roman_numeral(arabic)
    return _apply_subtractive_rule(purely_additive_roman)

