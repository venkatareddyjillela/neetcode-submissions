class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = []
        for k, v in count.items():
            heapq.heappush(max_heap, (-v, k))
        
        q = deque()
        res = ''
        print("count:", count)
        while max_heap or q:
            pending = []
            if max_heap:
                if res and res[-1] == max_heap[0][1]:
                    break
                i, ch = heapq.heappop(max_heap)
                res += ch
                if i+1:
                    pending = [i+1, ch]
                
                print("res:", res)
            if q:
                i, ch = q.popleft()
                heapq.heappush(max_heap, (i, ch))
            if pending:
                q.append((pending[0], pending[1]))
            print("q:", q)

        return '' if max_heap else res
            