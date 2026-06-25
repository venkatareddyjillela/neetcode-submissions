class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and (n not in seen):
            digit = 0
            seen.add(n)
            while n:
                digit += (n % 10) ** 2
                n = n // 10
            n = digit

        return n == 1