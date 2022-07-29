import pytest

from src.string.length_of_longest_subarray import LongestSubarray


class TestLongestSubarray:
    @pytest.mark.parametrize(
        "input_, expected", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0)]
    )
    def test_solution_1(self, input_, expected):
        x = LongestSubarray()

        assert x.solution_1(input_) == expected
