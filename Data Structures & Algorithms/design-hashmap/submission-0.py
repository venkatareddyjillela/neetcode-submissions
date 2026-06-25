class MyHashMap:

    def __init__(self):
        self.hashMap = []
        

    def put(self, key: int, value: int) -> None:
        for i, kv in enumerate(self.hashMap):
            k, v = kv
            if key == k:
                self.hashMap[i] = (key, value)
                return
        self.hashMap.append((key, value))
            

    def get(self, key: int) -> int:
        for k, v in self.hashMap:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, kv in enumerate(self.hashMap):
            k, v = kv
            if key == k:
                self.hashMap.pop(i)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)