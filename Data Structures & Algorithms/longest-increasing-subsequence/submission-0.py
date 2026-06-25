class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = [0]
        def dfs(i, arr, currCount):
            if i >= n:
                for i in range(1, len(arr)):
                    if arr[i] <= arr[i-1]:
                        return

                maxLen[0] = max(maxLen[0], currCount)
                return
            
            arr.append(nums[i])
            dfs(i+1, arr, currCount+1)

            arr.pop()
            dfs(i+1, arr, currCount)

            return
        dfs(0, [], 0)
        return maxLen[0]