import pytest
import unittest
from arabic_to_roman_numeral import arabic_to_roman_numeral


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_arabic_to_roman_numeral(self):
        assert arabic_to_roman_numeral("1904") == "MCMIV"


if __name__ == "__main__":
    unittest.main()
