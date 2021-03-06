import pytest
import unittest
from arabic_to_roman_numeral import (arabic_to_roman_numeral,
                                     _arabic_to_additive_roman_numeral,
                                     _apply_subtractive_rule,
                                     _get_decimal_split,
                                     _simple_arabic_to_roman)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_arabic_to_roman(self):
        assert _simple_arabic_to_roman("400") == "CCCC"
        assert _simple_arabic_to_roman("900") == "DCCCC"
        assert _simple_arabic_to_roman("0") == ""
        assert _simple_arabic_to_roman("1") == "I"
        assert _simple_arabic_to_roman("2900") == "MMDCCCC"

    def test_get_decimal_split(self):
        assert _get_decimal_split("1904") == ["1000", "900", "0", "4"]

    def test_arabic_to_additive_roman_numeral(self):
        assert _arabic_to_additive_roman_numeral("1904") == "MDCCCCIIII"

    def test_apply_subtractive_rule(self):
        assert _apply_subtractive_rule("MDCCCCIIII") == "MCMIV"

    def test_arabic_to_roman_numeral(self):
        assert arabic_to_roman_numeral("1904") == "MCMIV"
        assert arabic_to_roman_numeral("1954") == "MCMLIV"
        assert arabic_to_roman_numeral("1990") == "MCMXC"
        assert arabic_to_roman_numeral("2014") == "MMXIV"


if __name__ == "__main__":
    unittest.main()
