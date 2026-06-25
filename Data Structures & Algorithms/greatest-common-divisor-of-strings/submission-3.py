class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return ''
        # res = ''
        # m, n = len(str1), len(str2)
        # min_str = str1 if m < n else str2
        # max_str = str2 if m < n else str1
        # i = 0
        # while i < len(min_str):
        #     i += 1
        #     if len(min_str) % i:
        #         continue
        #     multiple = len(min_str) // i
        #     if min_str[:i] * multiple == min_str:
        #         if len(max_str) % i:
        #             continue
        #         multiple = len(max_str) // i
        #         if min_str[:i] * multiple == max_str:
        #             res = min_str[:i]
        def isDivisor(l):
            if l1 % l or l2 % l:
                return False
            f1, f2 = l1 // l, l2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
        l1, l2 = len(str1), len(str2)
        for l in range(min(l1, l2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ''
            
            