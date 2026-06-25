from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = [-v for v in count.values()]
        heapq.heapify(freq)
        timeReq = 0
        q = deque()
        while freq or q:
            timeReq += 1
            if freq:
                cnt = 1+heapq.heappop(freq)
                if cnt:
                    q.append([cnt, timeReq+n])

            if q and q[0][1] == timeReq:
                heapq.heappush(freq, q.popleft()[0])
            
        return timeReq
            
            