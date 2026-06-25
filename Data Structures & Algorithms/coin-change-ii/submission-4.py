class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, total):
            if total >= amount or i == len(coins):
                if total == amount:
                    return 1
                return 0

            if (i, total) in dp:
                return dp[(i, total)] 
            
            dp[(i, total)] = dfs(i, total+coins[i]) + dfs(i+1, total)
            return dp[(i, total)]
        
        return dfs(0, 0)