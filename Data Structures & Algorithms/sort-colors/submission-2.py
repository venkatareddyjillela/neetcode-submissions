class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one = 0
        zero = 0
        two = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            else:
                two += 1
        
        nums[:] = [0] * zero + [1] * one + [2] * two