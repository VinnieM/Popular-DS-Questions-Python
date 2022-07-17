import pytest

from src.matrix.transpose import Transpose


class TestTranspose:
    @pytest.mark.parametrize(
        "input_, expected", [([[1, 1, 1], [2, 2, 2], [3, 3, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
                            ([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],
                             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
                            ]
    )
    def test_solution_1_returns_expected_result(self, input_, expected):
        matrix_transpose = Transpose()

        assert matrix_transpose.solution_1(input_) == expected
