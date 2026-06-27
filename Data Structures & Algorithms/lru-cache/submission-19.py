class Node:
    def __init__(self, key=0, value=0, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, next = node.prev, node.nxt
        prev.nxt, next.prev = next, prev

    def add(self, node):
        prev = self.right.prev
        prev.nxt, node.prev = node, prev
        node.nxt, self.right.prev = self.right, node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]

        newNode = Node(key, value)
        self.add(newNode)
        self.cache[key] = newNode

        if len(self.cache) > self.cap:
            leastUsed = self.left.nxt
            self.remove(leastUsed)
            del self.cache[leastUsed.key]
        
