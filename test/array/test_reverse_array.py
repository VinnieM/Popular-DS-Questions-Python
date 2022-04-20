import pytest

from src.array.reverse_array import ReverseArray


class TestReverseArray:
    @pytest.mark.parametrize(
        "input_string, expected", [("Hello", "olleH"), ("abc", "cba"), (None, None)]
    )
    def test_reverse_array_solution_1_returns_expected_result(
        self, input_string, expected
    ) -> None:
        reverse = ReverseArray()

        assert reverse.solution_1(input_string) == expected

    @pytest.mark.parametrize(
        "input_string, expected", [("Hello", "olleH"), ("abc", "cba"), (None, None)]
    )
    def test_reverse_array_solution_2_returns_expected_result(
            self, input_string, expected
    ) -> None:
        reverse = ReverseArray()

        assert reverse.solution_2(input_string) == expected

    @pytest.mark.parametrize(
        "input_string, expected", [("Hello", "olleH"), ("abc", "cba"), (None, None)]
    )
    def test_reverse_array_solution_3_returns_expected_result(
            self, input_string, expected
    ) -> None:
        reverse = ReverseArray()

        assert reverse.solution_3(input_string) == expected
