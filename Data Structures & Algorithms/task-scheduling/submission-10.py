class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # max_heap = []
        # heapq.heapify(max_heap)
        # for k, v in count.items():
        #     heapq.heappush(max_heap, [-v, 1])
        # q = deque()
        # curr_time = 0
        # while max_heap or q:
        #     curr_time += 1
        #     # if max_heap[0][1] > curr_time:
        #     #     continue

        #     if max_heap:
        #         task = heapq.heappop(max_heap)
        #         if task[0] < -1:
        #             task = [task[0]+1, task[1]+n+1]
        #             # print("task:", task)
        #             # heapq.heappush(max_heap, task)
        #             q.append(task)
        #     if q and q[0][1] == curr_time:
        #         heapq.heappush(max_heap, q.popleft())
            
        # return curr_time
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
        


            