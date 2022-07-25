import pytest

from src.general.palindrome_number import PalindromeNumber


class TestPalindromeNumber:
    @pytest.mark.parametrize(
        "input_, expected",
        [
            (121, True),
            (-121, False),
            (0, True),
            (10, False),
            (11, True),
            (12321, True),
            (None, False),
            ("ABC", False),
        ],
    )
    def test_solution_1(self, input_, expected):
        reverse_palindrome = PalindromeNumber()
        assert reverse_palindrome.solution_1(input_) == expected
