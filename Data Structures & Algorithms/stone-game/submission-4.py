class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            even = False if (r-l+1) % 2 else True
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l, r)] = max(dfs(l+1, r) + left, dfs(l, r-1) + right)
            return dp[(l, r)]
            
        alice_score = dfs(0, len(piles)-1)
        total_stones = sum(piles)
        return True if alice_score > total_stones - alice_score else False
