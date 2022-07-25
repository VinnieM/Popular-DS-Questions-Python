class PalindromeNumber:
    def solution_1(self, x: int) -> bool:
        if not isinstance(x, int) or x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number: int = 0
        while x > reverted_number:
            reverted_number = (reverted_number * 10) + (x % 10)
            x //= 10

        reverted_number = int(reverted_number)
        return x == reverted_number or x == reverted_number // 10
