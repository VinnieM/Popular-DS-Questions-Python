from typing import Union


class ReverseArray:
    def solution_1(self, string_to_reverse: str) -> Union[str, None]:
        if not string_to_reverse:
            return
        return string_to_reverse[::-1]

    def solution_2(self, string_to_reverse: str) -> Union[str, None]:
        if not string_to_reverse:
            return
        return "".join(reversed(string_to_reverse))

    def solution_3(self, string_to_reverse: str) -> Union[str, None]:
        if not string_to_reverse:
            return
        low = 0
        high = len(string_to_reverse) - 1
        to_char_array = list(string_to_reverse)
        while low < high:
            temp = to_char_array[low]
            to_char_array[low] = to_char_array[high]
            to_char_array[high] = temp
            low += 1
            high -= 1
        return "".join(to_char_array)
