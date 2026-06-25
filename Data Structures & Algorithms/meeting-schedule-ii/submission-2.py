"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        count = 0
        i, j = 0, 0
        n = len(start)
        max_count = 0
        while i < n and j < n:
            if start[i] < end[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            max_count = max(max_count, count)
        return max_count