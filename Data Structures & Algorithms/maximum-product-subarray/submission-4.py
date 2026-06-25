class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        for l in range(len(nums)):
            curr = nums[l]
            res = max(res, curr)
            for r in range(l+1, len(nums)):
                curr *= nums[r]
                res = max(res, curr)
        
        return res