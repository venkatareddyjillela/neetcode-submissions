class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        maxP = nums[0]

        for num in nums:
            temp = currMax * num
            currMax = max(temp, currMin * num, num)
            currMin = min(temp, currMin * num, num)
            maxP = max(maxP, currMax)
        
        return maxP
