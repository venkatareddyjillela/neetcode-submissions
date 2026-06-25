from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val = self.hashmap[key]
        for i, item in enumerate(val):
            if item[0] == timestamp:
                return item[1]
            elif item[0] > timestamp:
                if val[i-1][0] < timestamp:
                    return val[i-1][1]
        return val[-1][1] if val and val[-1][0] < timestamp else ''


