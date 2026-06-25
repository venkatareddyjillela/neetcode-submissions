class MyHashMap:

    def __init__(self):
        self.hash_map = []

    def put(self, key: int, value: int) -> None:
        for i, kv in enumerate(self.hash_map):
            if key == kv[0]:
                self.hash_map[i] = (key, value)
                return
        self.hash_map.append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.hash_map:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, kv in enumerate(self.hash_map):
            if kv[0] == key:
                self.hash_map.pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)