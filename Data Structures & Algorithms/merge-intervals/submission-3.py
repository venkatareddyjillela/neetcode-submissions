class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        res.append(intervals[0])

        for i in intervals[1:]:
            if res[-1][1] < i[0]:
                res.append(i)
            else:
                newInterval = [min(res[-1][0], i[0]), max(res[-1][1], i[1])]
                res[-1] = newInterval
        
        return res

