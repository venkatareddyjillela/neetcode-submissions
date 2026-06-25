class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def append(self, node):
        prv = self.right.prev
        prv.next = node
        node.prev = prv
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        else:
            if len(self.cache) == self.cap:
                node = self.left.next
                self.remove(node)
                del self.cache[node.key]
        node = ListNode(key, value)
        self.append(node)
        self.cache[key] = node
            
