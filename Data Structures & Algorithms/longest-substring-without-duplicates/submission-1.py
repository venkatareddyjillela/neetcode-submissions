class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        hash_set = set()
        l = 0
        n = len(s)
        curr = 0

        for r in range(n):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                curr -= 1
                l += 1

            curr += 1
            hash_set.add(s[r])
            longest = max(longest, curr)

        return longest