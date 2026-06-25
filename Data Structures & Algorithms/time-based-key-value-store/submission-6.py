from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val = self.hashmap[key]
        if not val:
            return ''
        # for i, item in enumerate(val):
        l, r = 0, len(val)-1
        while l <= r:
            mid = (l+r)//2
            item = val[mid]
            if item[0] == timestamp:
                return item[1]
            elif item[0] > timestamp:
                if val[mid-1][0] < timestamp:
                    return val[mid-1][1]
                r = mid-1
            else:
                l = mid+1
        return val[-1][1] if val[-1][0] < timestamp else ''


