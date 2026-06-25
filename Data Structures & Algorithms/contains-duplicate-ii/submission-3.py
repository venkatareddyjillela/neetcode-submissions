class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set = set()
        l, r = 0, 0
        n = len(nums)

        while r < n and r <= k:
            if nums[r] in hash_set:
                return True
            hash_set.add(nums[r])
            r += 1
        
        while r < n:
            hash_set.remove(nums[l])
            if nums[r] in hash_set:
                return True
            hash_set.add(nums[r])
            r += 1
            l += 1
        
        return False
