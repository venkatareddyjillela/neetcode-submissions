class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum = sum(stones)
        target = math.ceil(stonesSum / 2)
        dp = {}

        def dfs(i, total):
            if total >= target or i >= len(stones):
                return abs(total - (stonesSum - total))
            if(i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = min(dfs(i+1, total+stones[i]), dfs(i+1, total))
            return dp[(i, total)]
        
        return dfs(0, 0)

