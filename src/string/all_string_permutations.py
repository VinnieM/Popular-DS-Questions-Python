from typing import List


class StringPermutation:
    def solution_1(self, string: List[str], low: int, high: int):
        if low == high:
            print("".join(string))
        else:
            for each_element in range(low, high):
                string[low], string[each_element] = string[each_element], string[low]
                self.solution_1(string, low + 1, high)
                string[low], string[each_element] = string[each_element], string[low]
