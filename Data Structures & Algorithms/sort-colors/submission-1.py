class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # R = n-1
        # L = 0
        # while L < R:
        #     while L < R and nums[R] == 2:
        #         R -= 1
        #     if nums[L] == 2:
        #         nums[R], nums[L] = nums[L], nums[R]
        #         R -= 1
        #     L += 1
        
        # while R >= 0 and nums[R] == 2:
        #     R -= 1

        # L = 0
        # while L < R:
        #     while L < R and nums[R] == 1:
        #         R -= 1
        #     if nums[L] == 1:
        #         nums[R], nums[L] = nums[L], nums[R]
        #         R -= 1
        #     L += 1

        L, R = 0, len(nums)-1
        i = 0

        while i <= R:
            if nums[i] == 0:
                nums[i], nums[L] = nums[L], nums[i]
                L += 1
            elif nums[i] == 2:
                nums[i], nums[R] = nums[R], nums[i]
                R -= 1
                i -= 1
            i += 1
        