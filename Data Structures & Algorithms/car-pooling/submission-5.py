class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        heapq.heapify(heap)

        for numPass, frm, to in trips:
            heapq.heappush(heap, [frm, to, numPass])
        curr = 0
        q = deque()
        while heap:
            frm, to, numPass = heapq.heappop(heap)
            while q and q[0][0] <= frm:
                _, cnt = q.popleft()
                curr -= cnt
            curr += numPass
            if curr > capacity:
                return False
            q.append([to, numPass])
        
        return True