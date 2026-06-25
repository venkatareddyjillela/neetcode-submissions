class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum, curr_sum = nums[0], 0

        for num in nums:
            curr_sum = max(curr_sum+num, num)
            global_sum = max(global_sum, curr_sum)
        return global_sum