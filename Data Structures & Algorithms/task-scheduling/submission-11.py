class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        heapq.heapify(heap)
        for _, v in count.items():
            heapq.heappush(heap, -v)
        
        q = deque()
        curr_time = 0
        while q or heap:
            curr_time += 1
            if heap:
                val = 1 + heapq.heappop(heap)
                if val:
                    q.append([val, curr_time+n])
            if q and q[0][1] == curr_time:
                heapq.heappush(heap, q.popleft()[0])
        
        return curr_time
        


            