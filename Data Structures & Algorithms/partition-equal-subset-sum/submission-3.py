class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums)//2
        n = len(nums)
        dp = [[-1] * (target+1) for _ in range(n)]
        
        def dfs(i, curr):
            if curr > target:
                return False

            if i >= n:
                return curr == target

            if dp[i][curr] != -1:
                return dp[i][curr]

            dp[i][curr] = dfs(i+1, curr) or dfs(i+1, curr+nums[i])
            
            return dp[i][curr]

        return dfs(0, 0)


            
            
