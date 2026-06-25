class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # pool = []
        # heapq.heapify(pool)
        # for trip in trips:
        #     heapq.heappush(pool, [trip[1], trip[2], trip[0]])
        
        # curr_occupy = 0
        # prev_dest = 0
        # while pool:
        #     start, dest, num_pass = heapq.heappop(pool)
        #     if num_pass > capacity:
        #         return False
            
        #     if start < prev_dest:
        #         if curr_occupy + num_pass > capacity:
        #             return False
        #         else:
        #             curr_occupy += num_pass
        #     else:
        #         curr_occupy = num_pass

        #     prev_dest = max(prev_dest, dest)
        
        # return True

        trips.sort(key = lambda t:t[1])
        min_heap = [] # [2, 4]
        curr_pass = 0 # 4
        # curr_dest = 0
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












