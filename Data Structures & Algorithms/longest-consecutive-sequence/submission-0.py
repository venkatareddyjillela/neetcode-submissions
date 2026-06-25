from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = Counter(nums)
        longest = 0
        for k in count:
            curr_long = 0
            if k - 1 in count:
                continue
            val = k
            while curr_long < len(count.keys()):
                if val in count:
                    curr_long += 1
                    val += 1
                else:
                    break
                longest = max(curr_long, longest)
        return longest