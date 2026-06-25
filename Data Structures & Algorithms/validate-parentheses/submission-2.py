from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        store = defaultdict(int)
        par_list = []
        for i in range(len(s)):
            if s[i] not in par_map:
                par_list.append(s[i])
            else:
                if (not par_list) or (par_list[-1] != par_map[s[i]]): return False
                par_list.pop()
        
        return len(par_list) == 0