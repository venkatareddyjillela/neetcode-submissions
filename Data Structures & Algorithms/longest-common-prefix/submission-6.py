class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Vertical scanning (checking each index of all strings) - O(m*n), O(1)
        if not strs:
            return ""
        res = strs[0]
        for i in range(len(res)):
            for s in strs:
                if i == len(s) or s[i] != res[i]:
                    return res[:i]
        
        return res