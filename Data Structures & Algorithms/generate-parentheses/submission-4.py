class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        openN, closedN = 0, 0
        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack.copy()))
                return
            
            if openN < n:
                stack.append('(')
                dfs(openN+1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(')')
                dfs(openN, closedN+1)
                stack.pop()
        dfs(openN, closedN)
        return res