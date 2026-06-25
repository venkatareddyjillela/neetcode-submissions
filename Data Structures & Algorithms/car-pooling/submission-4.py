class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        min_heap = [] 
        curr_pass = 0 
        for trip in trips:
            passengers, start, dest = trip
            curr_pass += passengers
            while min_heap and min_heap[0][0] <= start:
                curr_pass -= min_heap[0][1]
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, [dest, passengers])

            if curr_pass > capacity:
                return False

        return True












