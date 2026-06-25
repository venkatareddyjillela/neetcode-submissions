class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        pick = [False] * n

        def dfs(curr, pick):
            if len(curr) == n:
                res.append(curr.copy())
                return
            
            for i in range(n):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    dfs(curr, pick)
                    curr.pop()
                    pick[i] = False
        dfs([], pick)
        return res

