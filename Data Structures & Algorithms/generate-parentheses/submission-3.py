class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, opn, cls):
            if opn > n or cls > n or cls > opn:
                return
            if opn == cls == n:
                res.append(curr)
                return

            dfs(curr+'(', opn+1, cls)
            dfs(curr+')', opn, cls+1)
        
        dfs('', 0, 0)
        return res
        