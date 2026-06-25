class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            start_new, end_new = newInterval
            start, end = interval
            if end < start_new:
                res.append(interval)
            elif end_new < start:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                newInterval = [min(start, start_new), max(end, end_new)]

        res.append(newInterval)
        return res
