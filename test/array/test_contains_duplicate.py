import pytest

from src.array.contains_duplicate import ContainsDuplicate


class TestContainsDuplicate:
    @pytest.mark.parametrize(
        "input_, expected",
        [
            ([1, 2, 3, 4, 1], True),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),
            ([], False),
        ],
    )
    def test_solution_1(self, input_, expected):
        duplicate = ContainsDuplicate()

        assert duplicate.solution_1(input_) == expected
