class Solution:
    def longestPalindrome(self, s: str) -> str:
    #     max_pali = 0
    #     L, R = -1, -1
    #     for l in range(len(s)):
    #         for r in range(l, len(s)):
    #             if self.isPali(s, l, r):
    #                 curr = r-l+1
    #                 if curr > max_pali:
    #                     max_pali = curr
    #                     L = l
    #                     R = r
    #     return s[L:R+1]

    # def isPali(self, s, l, r):
    #     while l < r:
    #         if s[l] != s[r]:
    #             return False
    #         l += 1
    #         r -= 1
    #     return True

        L, R = -1, -1
        subStrL = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > subStrL:
                    subStrL = r-l+1
                    L, R = l, r
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > subStrL:
                    subStrL = r-l+1
                    L, R = l, r
                l -= 1
                r += 1
        return s[L:R+1]