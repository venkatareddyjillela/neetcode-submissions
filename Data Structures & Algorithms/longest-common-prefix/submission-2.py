class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return res

        sample = strs[0]

        ind = 0
        while ind < len(sample):
            for s in strs:
                if ind >= len(s) or sample[ind] != s[ind]:
                    return s[:ind]
            ind += 1
        
        return strs[0]

                
