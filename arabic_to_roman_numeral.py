def _simple_arabic_to_roman(simple_arabic):
    pass


def _get_decimal_split(arabic):
    pass


def _arabic_to_additive_roman_numeral(arabic):
    # For e.g. "1904"
    # Split into pieces per decimal place, e.g. ["1000", "900", "0", "4"].
    # Then per number in this list, replace by the largest roman number
    # if equal to it, if not ...
    dsplit = _get_decimal_split(arabic)
    rsplit = [_simple_arabic_to_roman(num) for num in dsplit]
    return "".join(rsplit)


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

