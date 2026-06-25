class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        def dfs(i):
            if i == n-1:
                return True
            if nums[i] == 0:
                return False
            
            for j in range(1, nums[i]+1):
                if i + j < n:
                    if dfs(i+j):
                        return True
            return False
        return dfs(0)