from typing import List, Tuple, Optional


class MinAndMaxElement:
    def solution_1(self, number_array: List[int]) -> Optional[Tuple]:
        if not number_array:
            return
        return min(number_array), max(number_array)

    def solution_2(self, number_array: List[int]) -> Optional[Tuple]:
        if not number_array:
            return
        min_element = number_array[0]
        max_element = number_array[0]
        for count, current_element in enumerate(number_array, start=1):
            if current_element > max_element:
                max_element = current_element
            if current_element < min_element:
                min_element = current_element
        return min_element, max_element
