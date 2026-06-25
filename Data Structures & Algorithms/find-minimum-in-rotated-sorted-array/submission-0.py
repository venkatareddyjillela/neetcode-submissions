class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = nums[0]

        while L <= R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            mid = (L+R)//2
            res =  min(res, nums[mid])
            if nums[R] <= nums[mid]:
                L = mid + 1
            else:
                R = mid - 1

        return res