class ListNode:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.hashmap = {}
        self.right.prev = self.left
        self.left.next = self.right

    def append(self, node):
        prev = self.right.prev
        node.prev = prev
        node.next = self.right
        prev.next = node
        self.right.prev = node
        return node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap.get(key)
        self.remove(node)
        node = self.append(node)
        self.hashmap[key] = node
        return node.val
        

    def put(self, key: int, value: int) -> None:
        new_node = ListNode(key, value)
        if key in self.hashmap:
            node = self.hashmap.get(key)
            self.remove(node)
            new_node = self.append(new_node)
            self.hashmap[key] = new_node
        
        else:
            if len(self.hashmap) == self.cap:
                node = self.left.next
                self.remove(node)
                del self.hashmap[node.key]
            
            self.append(new_node)
            self.hashmap[key] = new_node



