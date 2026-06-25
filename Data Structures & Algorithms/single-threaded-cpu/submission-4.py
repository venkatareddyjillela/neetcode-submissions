class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        available = []
        res = []
        heapq.heapify(pending)
        heapq.heapify(available)
        for i, [enqueueTimei, processingTimei] in enumerate(tasks):
            heapq.heappush(pending, [enqueueTimei, processingTimei, i])
        curr_time = 0
        while pending or available:
            while pending and pending[0][0] <= curr_time:
                enqueueTimei, processingTimei, i = heapq.heappop(pending)
                heapq.heappush(available, [processingTimei, i])
            
            if not available:
                curr_time = pending[0][0]
                continue
            
            processingTimei, i = heapq.heappop(available)
            curr_time += processingTimei
            res.append(i)
        
        return res
            