class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMin, currMax, globalMin, globalMax = 0, 0, nums[0], nums[0]
        total = 0

        for n in nums:
            currMin = min(currMin+n, n)
            currMax = max(currMax+n, n)
            globalMin = min(globalMin, currMin)
            globalMax = max(globalMax, currMax)
            total += n

        if globalMax < 0:
            return globalMax   
        
        return max(globalMax, total - globalMin)
