class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        def dfs(alice, i, M):
            if i == n:
                return 0
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]

            res = 0 if alice else float('inf')
            total = 0
            for X in range(1, 2*M + 1):
                if X + i > n:
                    break
                
                total += piles[X+i-1]

                if alice:
                    res = max(res, total + dfs(not alice, X+i, max(X, M)))
                else:
                    res = min(res, dfs(not alice, X+i, max(X, M)))
            dp[(alice, i, M)] = res
            return res
        
        return dfs(True, 0, 1)
