class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        res = [nums[0], 0]
        while l <= r:
            if nums[l] < nums[r]:
                if res[0] > nums[l]:
                    res = [nums[l], l]
                l = r

            mid = (l+r)//2
            if nums[mid] < res[0]:
                res = [nums[mid], mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
            
        pivot = res[1]
        nums = nums[pivot:] + nums[:pivot]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            val = nums[mid]
            if val == target:
                if pivot + mid < len(nums):
                    return pivot + mid
                else:
                    return (pivot+mid) - len(nums)
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1