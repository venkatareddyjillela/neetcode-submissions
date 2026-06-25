class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if that num is starting of sequence
        no_dup = set(nums)
        longest = 0
        for num in no_dup:
            if num-1 in no_dup:
                continue
            curr = 1
            while num + 1 in no_dup:
                curr += 1
                num += 1
            longest = max(longest, curr)
        
        return longest
