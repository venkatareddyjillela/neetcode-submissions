class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        L, R = 0, 0
        maxL = 0
        nodup = set()
        while L <= R and R < n:
            if s[R] in nodup:
                nodup.remove(s[L])
                L += 1
            else:
                nodup.add(s[R])
                R += 1
            maxL = max(maxL, len(nodup))
        return maxL