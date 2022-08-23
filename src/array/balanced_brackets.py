class BalancedBrackets:
    def solution_1(self, s: str) -> bool:
        if not s:
            return False
        dict_ = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for each_element in s:
            if each_element in dict_:
                stack.append(each_element)
            elif len(stack) == 0 or dict_[stack.pop()] != each_element:
                return False
        return len(stack) == 0
