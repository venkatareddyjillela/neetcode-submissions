class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0

        prev = intervals[0]
        for i in intervals[1:]:
            if prev[1] <= i[0]:
                prev = i
            else:
                prev[1] = min(prev[1], i[1])
                count += 1
        
        return count