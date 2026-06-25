class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        def dfs(i):
            curr_gas = 0
            for j in range(i, n):
                curr_gas += gas[j]
                if cost[j] > curr_gas:
                    return False
                curr_gas -= cost[j]
            
            for j in range(0, i):
                curr_gas += gas[j]
                if cost[j] > curr_gas:
                    return False
                curr_gas -= cost[j]
            
            return True

        for i in range(n):
            if dfs(i):
                return i

        return -1