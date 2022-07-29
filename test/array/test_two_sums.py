import pytest

from src.array.two_sums import TwoSums


class TestTwoSums:
    @pytest.mark.parametrize(
        "input_1, input_2, expected", [([2, 1, 5, 3], 4, [1, 3]), ([2, 4, 2, 1, 5, 3, 5], 10, [4, 6])]
    )
    def test_solution_1(self, input_1, input_2, expected):
        two_sums = TwoSums()

        assert two_sums.solution_1(input_1, input_2) == expected
