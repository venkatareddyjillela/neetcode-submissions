class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = []
        prev = intervals[0]
        for i in range(1, n):
            if prev[1] < intervals[i][0]:
                res.append(prev)
                prev = intervals[i]
            else:
                prev[1] = max(prev[1], intervals[i][1])

        res.append(prev)
        return res
