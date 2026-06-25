class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # curr = []
        res = [0]
        def dfs(i, currLen, currMax):
            if i == len(nums):
                res[0] = max(currLen, res[0])
                return
            
            if nums[i] > currMax:
                # curr.append(nums[i])
                dfs(i+1, currLen+1, nums[i])
                # curr.pop()
            dfs(i+1, currLen, currMax)

        dfs(0, 0, -float('inf'))
        return res[0]