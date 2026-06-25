class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curr = []
        res = [-float('inf')]
        def dfs(i, currMax):
            if i == len(nums):
                res[0] = max(len(curr), res[0])
                return
            
            if nums[i] > currMax:
                curr.append(nums[i])
                dfs(i+1, nums[i])
                curr.pop()
            dfs(i+1, currMax)

        dfs(0, -float('inf'))
        return res[0]