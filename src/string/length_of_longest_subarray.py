class LongestSubarray:
    def solution_1(self, string: str) -> int:
        if not string:
            return 0
        char_set = set()
        left_index = 0
        result = 0

        for right_index in range(len(string)):
            while string[right_index] in char_set:
                char_set.remove(string[left_index])
                left_index += 1
            char_set.add(string[right_index])
            result = max(result, right_index - left_index + 1)

        return result
