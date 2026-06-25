class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def dfs(i, curr):
            if len(nums) == i:
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1, curr)

            curr.pop()
            dfs(i+1,curr)

        dfs(0, [])
        sum_xor = 0
        for subset in res:
            if subset:
                subset_xor = 0
                for i in subset:
                    subset_xor ^= i
                sum_xor += subset_xor
        return sum_xor

