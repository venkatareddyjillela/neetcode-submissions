class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0

        L, R = 0, len(nums)-1

        while L <= R:
            mid = (L + R)//2
            val = nums[mid]
            print(val)
            if val == target:
                return mid
            elif val < target:
                L = mid+1
            else:
                R = mid - 1
        return -1