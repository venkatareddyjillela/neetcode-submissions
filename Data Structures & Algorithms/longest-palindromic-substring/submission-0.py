class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pali = 0
        L, R = -1, -1
        for l in range(len(s)):
            for r in range(l, len(s)):
                if self.isPali(s, l, r):
                    # max_pali = max(max_pali, r-l+1)
                    curr = r-l+1
                    if curr > max_pali:
                        max_pali = curr
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