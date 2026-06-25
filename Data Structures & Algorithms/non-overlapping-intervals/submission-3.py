class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        prev = intervals[0]
        for curr in intervals[1:]:
            if prev[1] <= curr[0]:
                prev = curr
            else:
                prev[1] = min(prev[1], curr[1])

                count += 1
        return count