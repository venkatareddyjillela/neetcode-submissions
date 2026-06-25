class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        curr = 0
        no_dup = set(nums)
        validated = set()

        for num in nums:
            if num in validated:
                continue
            validated.add(num)
            curr = 1
            curr_num = num
            while curr_num + 1 in no_dup:
                curr += 1
                validated.add(num+1)
                curr_num += 1
            
            longest = max(longest, curr)
        
        return longest