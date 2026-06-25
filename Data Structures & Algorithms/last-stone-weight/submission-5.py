class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]

        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, -abs(x-y))
        
        return -max_heap[0] if max_heap else 0