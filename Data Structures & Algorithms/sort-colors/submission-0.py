class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        R = n-1
        L = 0
        while L < R:
            while L < R and nums[R] == 2:
                R -= 1
            if nums[L] == 2:
                nums[R], nums[L] = nums[L], nums[R]
                R -= 1
            L += 1
        
        while R >= 0 and nums[R] == 2:
            R -= 1

        L = 0
        while L < R:
            while L < R and nums[R] == 1:
                R -= 1
            if nums[L] == 1:
                nums[R], nums[L] = nums[L], nums[R]
                R -= 1
            L += 1
        