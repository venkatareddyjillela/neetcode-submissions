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
            
            i = 0
            while i < n:
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    dfs(curr, pick)
                    curr.pop()
                    pick[i] = False
                    while i+1 < n and nums[i] == nums[i+1]:
                        i += 1
                i += 1
        dfs([], pick)
        return res
