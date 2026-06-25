class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = {}

        # def dfs(i):
        #     if i >= n:
        #         return 0
            
        #     if i in dp:
        #         return dp[i]
            
        #     dp[i] = nums[i] + max(dfs(i+2), dfs(i+3))
        #     return dp[i]
        
        # return max(dfs(0), dfs(1))

        # n = len(nums)
        # if n <= 2:
        #     return max(nums)
        # if n == 3:
        #     return max(nums[0]+nums[2], nums[1])

        # dp = [-1] * n
        # dp[-2:] = nums[-2:]
        # dp[-3] = nums[-3] + nums[-1]

        # for i in range(n-4, -1, -1):
        #     dp[i] = nums[i] + max(dp[i+2], dp[i+3])
        
        # return max(dp[0], dp[1])

        n = len(nums)
        if n <= 2:
            return max(nums)
        if n == 3:
            return max(nums[0]+nums[2], nums[1])

        one, two, three = nums[-1]+nums[-3], nums[-2], nums[-1]

        for i in range(n-4, -1, -1):
            temp = nums[i] + max(two, three)
            three = two
            two = one
            one = temp
        
        return max(one, two)





