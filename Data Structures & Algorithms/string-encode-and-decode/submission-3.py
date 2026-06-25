class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '@' + s
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        l = ''
        i = 0
        while i < len(s):
            if s[i] == '@':
                strs.append(s[i+1: i+1+int(l)])
                i = i+1+int(l)
                l = ''
            else:
                l += s[i]
                i += 1
        return strs