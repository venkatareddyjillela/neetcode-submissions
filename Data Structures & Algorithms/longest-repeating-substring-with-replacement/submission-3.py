class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)
        l, r = 0, 0
        n = len(s)
        longest = 0
        for r in range(n):
            hash_map[s[r]] += 1
            while r-l+1 - max(hash_map.values()) > k:
                hash_map[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest