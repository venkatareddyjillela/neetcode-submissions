class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k+1):
            tempPrices = prices.copy()
            for frm, to, prc in flights:
                if prices[frm] == float('inf'):
                    continue
                
                if prices[frm] + prc < tempPrices[to]:
                    tempPrices[to] = prices[frm] + prc
                
            prices = tempPrices
        
        if prices[dst] < float('inf'):
            return prices[dst]
        
        return -1
