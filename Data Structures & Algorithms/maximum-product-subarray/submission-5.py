class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        for l in range(len(nums)):
            curr = 1
            for r in range(l, len(nums)):
                curr *= nums[r]
                res = max(res, curr)
        
        return res