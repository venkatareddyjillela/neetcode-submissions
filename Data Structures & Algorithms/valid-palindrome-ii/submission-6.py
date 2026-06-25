class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.isPali(s[l:r]) or self.isPali(s[l+1: r+1])
            l += 1
            r -= 1
        return True
        

    def isPali(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True