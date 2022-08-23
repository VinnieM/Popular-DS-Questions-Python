class StringPermutation:

    def check_inclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_array = [0] * 26

        for i in range(len(s1)):
