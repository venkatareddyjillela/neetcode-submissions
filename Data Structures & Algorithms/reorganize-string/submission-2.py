class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-v, k] for k, v in count.items()]
        heapq.heapify(heap)

        output = ""
        q = deque()
        while heap or q:
            while q and output and output[-1] != q[0][1]:
                heapq.heappush(heap, q.popleft())
            
            if not heap:
                return ""
            
            cnt, ch = heapq.heappop(heap)
            output += ch
            if cnt + 1:
                q.append([cnt+1, ch])
        
        return output

