class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap_map = []
        if a:
            heapq.heappush(heap_map, (-a, "a"))
        if b:
            heapq.heappush(heap_map, (-b, "b"))
        if c:
            heapq.heappush(heap_map, (-c, "c"))

        res = []
        while heap_map:
            count, ch = heapq.heappop(heap_map)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not heap_map:
                    break
                count2, ch2 = heapq.heappop(heap_map)
                res.append(ch2)
                count2 += 1
                if count2:
                    heapq.heappush(heap_map, (count2, ch2))
                heapq.heappush(heap_map, (count, ch))
            else:
                res.append(ch)
                count += 1
                if count:
                    heapq.heappush(heap_map, (count, ch))

        return ''.join(res)

