class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = nums
        self.k = k
        heapq.heapify(self.max_heap)
        while len(self.max_heap) > self.k:
            heapq.heappop(self.max_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, val)
        if len(self.max_heap) > self.k:
            heapq.heappop(self.max_heap)
        return self.max_heap[0]
