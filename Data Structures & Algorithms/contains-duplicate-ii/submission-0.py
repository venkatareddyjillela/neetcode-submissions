class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        n = len(nums)
        i, j = 0, 1
        while j < n:

            if nums[i] == nums[j]:
                return True
            
            if abs(i - j) < k:
                j += 1
            elif i+1 < j:
                i += 1
            else:
                i += 1
                j += 1
        return False