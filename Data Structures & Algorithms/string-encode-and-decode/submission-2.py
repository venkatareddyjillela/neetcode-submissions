class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            l = len(s)
            res +=  str(l) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l_len = 1
            while s[i+l_len] != '#':
                l_len += 1
            l = int(s[i:i+l_len])
            new_str = s[i+l_len+1: i+l_len+1+l]
            print(new_str)
            res.append(new_str)
            i += l_len+l+1
        return res