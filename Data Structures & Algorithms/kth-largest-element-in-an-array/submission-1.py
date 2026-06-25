class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        while max_heap and k > 1:
            heapq.heappop(max_heap)
            k -= 1
        return -max_heap[0]