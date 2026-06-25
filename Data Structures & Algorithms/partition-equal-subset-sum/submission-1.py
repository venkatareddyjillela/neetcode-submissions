class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums)/2
        n = len(nums)

        def dfs(i, curr):
            if curr > target:
                return False
            if i >= n:
                return curr == target
            
            return dfs(i+1, curr) or dfs(i+1, curr+nums[i])

        return dfs(0, 0)


            
            
