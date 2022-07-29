class PalindromeNumber:
    """
    For more info refer to PEP 238v - https://peps.python.org/pep-0238/
    """

    def solution_1(self, x: int) -> bool:
        if not isinstance(x, int) or x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number: int = 0
        while x > reverted_number:
            reverted_number = (reverted_number * 10) + (x % 10)
            x //= 10

        return x == reverted_number or x == reverted_number // 10

    def reverse(self, x):
        negFlag = 1
        if x < 0:
            negFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])

        return 0 if x > pow(2, 31) else x * negFlag
