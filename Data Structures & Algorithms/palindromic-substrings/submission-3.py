class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for l in range(len(s)):
            r = l
            while r < len(s):
                if self.is_pali(s, l, r):
                    count += 1
                r += 1
        
        return count
        

    def is_pali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True