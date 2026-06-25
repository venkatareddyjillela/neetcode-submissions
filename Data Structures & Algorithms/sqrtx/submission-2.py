class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            m = (l+r)//2
            val = m ** 2
            if val == x:
                return m
            elif val > x:
                r = m-1
            else:
                l = m+1
        return l-1