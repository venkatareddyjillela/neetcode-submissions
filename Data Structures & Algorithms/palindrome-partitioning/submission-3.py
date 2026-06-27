class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, curr):
            if i == len(s):
                res.append(curr.copy())
                return
            
            l = i 
            for r in range(i, len(s)):
                if self.is_pali(s, l, r):
                    curr.append(s[l:r+1])
                    dfs(r+1, curr)
                    curr.pop()
            return

        dfs(0, [])
        return res

    def is_pali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True