class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        valid, l, r = self.isPali(s, l, r)
        if not valid:
            valid, i, j = self.isPali(s, l+1, r)
        if not valid:
            valid, i, j = self.isPali(s, l, r-1)
        
        return valid
        

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                print(l, r)
                return False, l, r
            l += 1
            r -= 1
        return True, l, r