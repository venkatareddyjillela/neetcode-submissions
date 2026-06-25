
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamp_values = self.time_map[key]
        if not timestamp_values:
            return ""
        left, right = 0, len(timestamp_values)-1

        while left <= right:
            mid = (left+right)//2
            item = timestamp_values[mid]

            if item[0] == timestamp:
                return item[1]
            elif item[0] > timestamp:
                if timestamp_values[mid-1][0] < timestamp:
                    return timestamp_values[mid-1][1]
                right = mid-1
            else:
                left = mid+1
        return timestamp_values[-1][1] if timestamp_values[-1][0] < timestamp else ""