class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force approach
        # max_prod = nums[0]
        # n = len(nums)
        # for i in range(n):
        #     currP = 1
        #     for j in range(i, n):
        #         currP *= nums[j]
        #         max_prod = max(max_prod, currP)
        
        # return max_prod

        # dp
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            temp = currMax * n
            currMax = max(temp, currMin * n, n)
            currMin = min(temp, currMin * n, n)
            res = max(res, currMax)
        
        return res