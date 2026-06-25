class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = len(nums)+1
        n = len(nums)
        l, r = 0, 0
        total = 0
        while r < n:
            total += nums[r]
            print("total", total)
            while total >= target:
                minL = min(minL, r-l+1)
                print(minL)
                total -= nums[l]
                l += 1
            r += 1
                

        return minL if minL != len(nums)+1 else 0