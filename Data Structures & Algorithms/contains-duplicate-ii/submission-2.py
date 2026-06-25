class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        n = len(nums)
        i = 0
        window = set()
        for j in range(n):
            if j - i > k:
                window.remove(nums[i])
                i += 1
            if nums[j] in window:
                return True
            window.add(nums[j])
        return False