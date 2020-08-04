from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key : int):
        """return the value of the key
        and move the accessed key to the front"""
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    def put(self, key: int, value: int) -> None:
        """keep track of capacity
        if full evict something"""
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(False)

    def run(self):
        lru = LRUCache(3)
        lru.put(1, 2)
        lru.put('a', 'b')
        print(lru)
lru = LRUCache(3)
lru.put(1,2)
lru.put('a','b')
print(LRUCache.run(lru))