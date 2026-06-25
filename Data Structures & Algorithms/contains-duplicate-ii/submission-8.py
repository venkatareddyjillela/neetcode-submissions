class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set = set()
        i = 0
        n = len(nums)

        for j in range(n):
            if j - i > k:
                hash_set.remove(nums[i])
                i += 1
            if nums[j] in hash_set:
                return True
            hash_set.add(nums[j])
        return False