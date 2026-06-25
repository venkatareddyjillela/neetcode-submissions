class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        n = len(nums)
        for i in range(n):
            currP = 1
            for j in range(i, n):
                currP *= nums[j]
                max_prod = max(max_prod, currP)
        
        return max_prod