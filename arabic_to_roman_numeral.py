from collections import deque


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
            residual = simple_ar - current_ar
            return current_rom + _simple_arabic_to_roman(residual)
        elif simple_ar == current_ar:
            return current_rom
        elif simple_ar == next_ar:
            return next_rom


def _get_decimal_split(arabic):
    split = deque([])
    for i, digit in enumerate(reversed(arabic)):
        positional_number = int(digit) * 10**i
        split.appendleft(str(positional_number))
    return list(split)


def _arabic_to_additive_roman_numeral(arabic):
    dsplit = _get_decimal_split(arabic)
    rsplit = [_simple_arabic_to_roman(num) for num in dsplit]
    return "".join(rsplit)


def _apply_subtractive_rule(purely_additive_roman):
    par = purely_additive_roman.replace("DCCCC", "CM")
    par = par.replace("CCCC", "CD")
    par = par.replace("LXXXX", "XC")
    par = par.replace("XXXX", "XL")
    par = par.replace("IIII", "IV")
    return par


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
