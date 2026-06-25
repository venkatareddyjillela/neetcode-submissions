class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = len(nums)+1
        n = len(nums)
        l, r = 0, 0
        total = 0
        while r < n:
            total += nums[r]
            while total >= target:
                minL = min(minL, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1

        return minL if minL != len(nums) + 1 else 0