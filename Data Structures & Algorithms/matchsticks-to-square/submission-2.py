class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 or max(matchsticks) > total/4:
            return False
        
        length = total / 4
        sides = [0] * 4

        def dfs(i, sides):
            if i == len(matchsticks):
                return True
            
            for j in range(len(sides)):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if dfs(i+1, sides):
                        return True
                    sides[j] -= matchsticks[i]
            
            return False
        
        return dfs(0, sides)