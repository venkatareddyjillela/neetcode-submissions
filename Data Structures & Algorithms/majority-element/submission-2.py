class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = {}
        for n in nums:
            if n in nums_map:
                nums_map[n] += 1
            else:
                nums_map[n] = 1
        for k, v in nums_map.items():
            if v > len(nums)/2:
                return k