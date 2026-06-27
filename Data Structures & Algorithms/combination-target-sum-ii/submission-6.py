class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, currSum):
            if i == n or currSum > target:
                if currSum == target:
                    res.append(curr.copy())
                return
            
            curr.append(candidates[i])
            dfs(i+1, currSum + candidates[i])

            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1

            curr.pop()
            dfs(i+1, currSum)
            
        
        dfs(0, 0)
        return res