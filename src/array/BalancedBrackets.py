class BalancedBrackets:
    def solution_1(self, bracket_to_check: str) -> bool:
        stack = []
        for each_element in bracket_to_check:
            if each_element == "(" or each_element == "[" or each_element == "{":
                stack.append(each_element)
            elif each_element == ")" or each_element == "]" or each_element == "}":
                stack.pop()

        return True if len(stack) == 0 else False


if __name__ == '__main__':
    bracket = BalancedBrackets()
    print(bracket.solution_1("[()]{}{[()()]()}"))
