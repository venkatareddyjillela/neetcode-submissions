class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, curr):
            if i == len(nums) or curr >= target:
                if curr == target:
                    res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i, curr+nums[i])
            subset.pop()
            dfs(i+1, curr)

        dfs(0, 0)
        return res