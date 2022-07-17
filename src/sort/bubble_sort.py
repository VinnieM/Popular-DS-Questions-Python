from typing import List


class BubbleSort:
    def solution_1_ascending(self, array_to_sort: List[int]):
        if not array_to_sort:
            return
        array_length = len(array_to_sort)
        for i in range(array_length - 1):
            for j in range(array_length - 1):
                if array_to_sort[j] > array_to_sort[j + 1]:
                    array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]

        return array_to_sort

    def solution_2_descending(self, array_to_sort: List[int]):
        if not array_to_sort:
            return
        array_length = len(array_to_sort)
        for i in range(array_length - 1):
            for j in range(array_length - 1):
                if array_to_sort[j] < array_to_sort[j + 1]:
                    array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]

        return array_to_sort
