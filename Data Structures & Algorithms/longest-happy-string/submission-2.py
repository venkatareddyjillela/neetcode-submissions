class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        heapq.heapify(heap)

        if a:
            heapq.heappush(heap, [-a, 'a'])
        if b:
            heapq.heappush(heap, [-b, 'b'])
        if c:
            heapq.heappush(heap, [-c, 'c'])

        output = ""
        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            if len(output) > 1 and output[-2] == output[-1] == ch1:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                output += ch2
                if cnt2 + 1:
                    heapq.heappush(heap, [cnt2+1, ch2])
                heapq.heappush(heap, [cnt1, ch1])
            else:
                output += ch1
                if cnt1 + 1:
                    heapq.heappush(heap, [cnt1+1, ch1])
        return output
                    
                