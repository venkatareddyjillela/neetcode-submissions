class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n
        for i, n in enumerate(nums):
            xor = xor ^ n ^ i
        
        return xor
