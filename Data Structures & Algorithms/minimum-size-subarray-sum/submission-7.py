class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n+1
        l, r= 0, 0
        curr = 0
        while r < n:
            curr += nums[r]

            while curr >= target:
                min_len = min(min_len, r-l+1)
                curr -= nums[l]
                l += 1
            
            # if curr == target:
            #     min_len = min(min_len, r-l+1)
            
            r += 1
        
        return 0 if min_len == n+1 else min_len