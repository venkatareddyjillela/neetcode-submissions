class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        currSum = 0
        count = 0
        for num in nums:
            currSum += num

            count += prefixSum.get(currSum-k, 0)
            prefixSum[currSum] = 1+prefixSum.get(currSum, 0)

        return count