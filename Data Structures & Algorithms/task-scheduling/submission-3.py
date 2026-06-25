class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = count.values()
        heap = [-v for v in heap]
        heapq.heapify(heap)
        q = deque()
        timeReq = 0
        while heap or q:
            timeReq += 1
            if heap:
                val = 1 + heapq.heappop(heap)

                if val:
                    q.append([val, timeReq+n])
                
            if q and q[0][1] == timeReq:
                heapq.heappush(heap, q.popleft()[0])
        
        return timeReq
            