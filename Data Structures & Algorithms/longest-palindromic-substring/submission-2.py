class Solution:
    def longestPalindrome(self, s: str) -> str:
        L, R = -1, -1
        maxL = -1
        for l in range(len(s)):
            for r in range(l, len(s)):
                if self.isPali(s, l, r):
                    curr = r-l+1
                    if curr > maxL:
                        maxL = curr
                        L = l
                        R = r
        
        return s[L:R+1]


    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True