import pytest

from src.array.min_and_max import MinAndMaxElement


class TestMinAndMaxElement:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ([1, 2, 3, 4, 5, 6], (1, 6)),
            ([5, 4, 3, 2, 1], (1, 5)),
            ([2, 5, 2, 5, 2, 5, 8, 3, 54, 21, 56, 32, 78, 23675, 213], (2, 23675)),
            (None, None)
        ],
    )
    def test_solution_1_return_expected_result(self, input, expected):
        min_and_max = MinAndMaxElement()

        assert min_and_max.solution_1(input) == expected

    @pytest.mark.parametrize(
        "input, expected",
        [
            ([1, 2, 3, 4, 5, 6], (1, 6)),
            ([5, 4, 3, 2, 1], (1, 5)),
            ([2, 5, 2, 5, 2, 5, 8, 3, 54, 21, 56, 32, 78, 23675, 213], (2, 23675)),
            (None, None)
        ],
    )
    def test_solution_2_return_expected_result(self, input, expected):
        min_and_max = MinAndMaxElement()

        assert min_and_max.solution_2(input) == expected