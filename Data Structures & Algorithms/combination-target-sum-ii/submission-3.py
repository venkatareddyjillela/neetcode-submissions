class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i, curr):
            if i == len(candidates) or curr >= target:
                if curr == target:
                    res.append(subset.copy())
                return
            
            subset.append(candidates[i])
            dfs(i+1, curr + candidates[i])

            subset.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr)
        dfs(0, 0)
        return res