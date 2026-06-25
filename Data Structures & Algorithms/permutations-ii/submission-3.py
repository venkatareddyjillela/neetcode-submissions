class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        pick = [False] * n

        def dfs(curr, pick):
            if len(curr) == n:
                res.append(curr.copy())
                return
            
            for i in range(n):
                if not pick[i]:
                    if i and nums[i] == nums[i-1] and not pick[i-1]:
                        continue
                    curr.append(nums[i])
                    pick[i] = True
                    dfs(curr, pick)
                    curr.pop()
                    pick[i] = False

        dfs([], pick)
        return res