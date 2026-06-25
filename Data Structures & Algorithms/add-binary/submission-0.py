class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            char = total % 2
            carry = total // 2
            res += str(char)
        if carry:
            res += str(carry)
        
        return res[::-1]