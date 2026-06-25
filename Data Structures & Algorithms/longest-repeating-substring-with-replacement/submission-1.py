from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        distinct = defaultdict(int)
        maxL = 0
        n = len(s)
        L, R = 0, 0
        while R < n and L <= R:
            distinct[s[R]] += 1
            val = distinct.values()
            if sum(val) - max(val) > k:
                distinct[s[L]] -= 1
                L += 1
            maxL = max(maxL, R-L+1)
            R += 1
        return maxL

