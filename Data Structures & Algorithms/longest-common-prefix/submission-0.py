class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return res

        sample = strs[0]

        ind = 0
        matched = True
        while matched and ind < len(sample):
            for s in strs:
                if ind >= len(s) or sample[ind] != s[ind]:
                    matched = False
                    break
            
            if matched:
                res += sample[ind]
            ind += 1
        
        return res

                
