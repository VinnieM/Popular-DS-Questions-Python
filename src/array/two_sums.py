from typing import List


class TwoSums:
    def solution_1(self, nums: List[int], target) -> List[int]:
        dict_ = {}
        for i, each_number in enumerate(nums):
            difference = target - each_number
            if difference in dict_:
                return [dict[difference], i]
            dict_[each_number] = i
