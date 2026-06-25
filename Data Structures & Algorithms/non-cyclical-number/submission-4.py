class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        i = 0
        while n != 1 and (n not in seen):
            digit = 0
            seen.add(n)
            while n:
                digit += (n % 10) ** 2
                n = n // 10
            n = digit
            i += 1

        return n == 1