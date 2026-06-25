class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        n = len(nums)
        for num in nums:
            hash_map[num] += 1
        
        for k, v in hash_map.items():
            if v > n/2:
                return k
