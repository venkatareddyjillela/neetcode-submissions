class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}

    def remove(self, node) -> None:
        prv = node.prev 
        nxt = node.next
        nxt.prev, prv.next = prv, nxt
        
    
    def insert(self, node) -> None:
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

