class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {n-1: True}
        
        for i in range(n-2, -1, -1):
            res = False

            for j in range(1, nums[i]+1):
                if i + j < n:
                    if dp[i+j]:
                        res = True
                        break
                else:
                    break

            dp[i] = res
        
        return dp[0]