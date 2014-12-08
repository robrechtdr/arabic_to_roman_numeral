def _simple_arabic_to_roman(simple_arabic):
    base_conv_table = [("1000","M"), ("500","D"), ("100","C"),
                       ("50", "L"), ("10", "X"), ("5", "V"), ("1", "I"),
                       ("0", "")]

    simple_ar = int(simple_arabic)
    for i, base in enumerate(base_conv_table):
        current_ar = int(base[0])
        current_rom = base[1]
        next_ar = int(base_conv_table[i + 1][0])
        next_rom = base_conv_table[i + 1][1]

        if simple_ar > current_ar:
            residual_ar = simple_ar - current_ar
            return current_rom + _simple_arabic_to_roman(residual_ar)
        elif current_ar > simple_ar > next_ar:
            residual_ar = simple_ar - next_ar
            return next_rom + _simple_arabic_to_roman(residual_ar)
        elif simple_ar == current_ar:
            return current_rom
        elif simple_ar == next_ar:
            return next_rom


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


