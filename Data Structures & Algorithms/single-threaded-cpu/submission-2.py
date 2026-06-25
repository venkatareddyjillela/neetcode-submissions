class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        available = []
        curr_time = 0
        res = []
        for i, (enqueTime, processTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueTime, processTime, i))
        task_map = {}
        while pending or available:
            while pending and pending[0][0] <= curr_time:
                enqueTime, processTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processTime, i))

            if not available:
                curr_time = pending[0][0]
                continue
            
            processTime, i = heapq.heappop(available)
            res.append(i)
            curr_time += processTime
        return res