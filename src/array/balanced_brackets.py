class BalancedBrackets:
    def solution_1(self, input_: str) -> bool:
        if not input_:
            return False
        stack = []
        for each_item in input_:
            if each_item == "{" or each_item == "[" or each_item == "(":
                stack.append(each_item)
            elif each_item == "}" or each_item == "]" or each_item == ")":
                if not stack:
                    return False
                stack.pop()

        return True if len(stack) == 0 else False
