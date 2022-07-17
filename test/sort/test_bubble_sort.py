import pytest

from src.sort.bubble_sort import BubbleSort


class TestBubbleSort:

    @pytest.mark.parametrize("input_, expected", [([], None), (None, None), ([2, 5, 4, 1, 3], [1, 2, 3, 4, 5])])
    def test_solution_1(self, input_, expected):
        bubble_sort = BubbleSort()

        assert bubble_sort.solution_1_ascending(input_) == expected

    @pytest.mark.parametrize("input_, expected", [([], None), (None, None), ([2, 5, 4, 1, 3], [5, 4, 3, 2, 1])])
    def test_solution_2(self, input_, expected):
        bubble_sort = BubbleSort()

        assert bubble_sort.solution_2_descending(input_) == expected
