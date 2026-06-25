class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0XFFFFFFFF
        MAX_INT = 0X7FFFFFFF
        while b != 0:
            xor = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = xor, carry
        
        return a if a <= MAX_INT else ~(a ^ MASK)
