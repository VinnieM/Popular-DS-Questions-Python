import pytest

from src.general.reverse_integer import ReverseInteger


class TestReverseInteger:
    @pytest.mark.parametrize(
        "input_, expected",
        [
            (123, 321), (-123,-321), (120, 21)
        ],
    )
    def test_solution_1(self, input_, expected):
        reverse_integer = ReverseInteger()
        assert reverse_integer.solution_1(input_) == expected
