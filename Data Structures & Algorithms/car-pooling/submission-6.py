class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        ongoing = []
        heapq.heapify(ongoing)
        currPass = 0
        for numPass, frm, to in trips:
            while ongoing and ongoing[0][0] <= frm:
                dst, cnt = heapq.heappop(ongoing)
                currPass -= cnt
            
            currPass += numPass
            if currPass > capacity:
                return False
            
            heapq.heappush(ongoing, [to, numPass])
        
        return True