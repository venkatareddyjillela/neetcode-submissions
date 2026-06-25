class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dup = set()
        for n in nums:
            if n in no_dup:
                return True
            no_dup.add(n)
        return False