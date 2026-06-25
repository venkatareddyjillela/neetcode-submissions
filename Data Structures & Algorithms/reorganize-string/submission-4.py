class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-v, k] for k, v in count.items()]
        heapq.heapify(heap)

        output = ""
        q = []
        while heap or q:
            pending = []
            if heap:
                if output and output[-1] == heap[0][1]:
                    break
                cnt, ch = heapq.heappop(heap)
                output += ch
                if cnt + 1:
                    pending = [cnt+1, ch]

            if q:
                heapq.heappush(heap, q)
                q = []
            
            if pending:
                q = pending
        
        return "" if heap else output