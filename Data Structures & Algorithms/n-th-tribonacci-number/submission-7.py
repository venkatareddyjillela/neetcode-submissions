class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        one, two, three = 1, 1, 0

        for i in range(n-2):
            temp = one + two + three
            three = two
            two = one
            one = temp
        
        return one