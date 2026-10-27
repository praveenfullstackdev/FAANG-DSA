"""
LeetCode 146: LRU Cache (Least Recently Used Cache)

FAANG Architecture:
Hash Map + Doubly Linked List with Sentinel (Dummy) Head & Tail
Time Complexity: Strict O(1) for both get() and put()
Space Complexity: O(capacity)
"""

class DListNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DListNode
        
        # Sentinel dummy nodes
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DListNode) -> None:
        """O(1) in-place node extraction."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: DListNode) -> None:
        """O(1) insertion directly after dummy head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)  # Mark as most recently used
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict least recently used (node right before dummy tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            new_node = DListNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1       # returns 1, marks 1 as MRU
    cache.put(3, 3)                # evicts key 2
    assert cache.get(2) == -1      # returns -1 (not found)
    cache.put(4, 4)                # evicts key 1
    assert cache.get(1) == -1      # returns -1 (not found)
    assert cache.get(3) == 3       # returns 3
    assert cache.get(4) == 4       # returns 4
    print("LRU Cache operations tested and verified successfully!")
