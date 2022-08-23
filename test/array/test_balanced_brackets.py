import pytest

from src.array.balanced_brackets import BalancedBrackets


class TestBalancedBrackets:
    @pytest.mark.parametrize(
        "input, expected", [("{[()]}", True), ("{}[((){}))]", False), ("(]", False)]
    )
    def test_solution_1(self, input, expected):
        balanced = BalancedBrackets()

        assert balanced.solution_1(input) == expected
