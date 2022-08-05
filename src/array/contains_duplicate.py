from typing import List


class ContainsDuplicate:

    def solution_1(self, nums: List[int]) -> bool:
        if not nums:
            return False

        hash_set = set()
        for each_number in nums:
            if each_number in hash_set:
                return True
            hash_set.add(each_number)

        return False
