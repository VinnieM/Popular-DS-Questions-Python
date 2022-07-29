class ReverseInteger:
    def solution_1(self, number: int) -> int:
        neg_flag = 1
        if number < 0:
            neg_flag = -1
            str_ = str(number)[1:]
        else:
            str_ = str(number)

        number = int(str_[::-1])
        return 0 if number > pow(2, 31) else number * neg_flag
