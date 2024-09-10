from collections import OrderedDict

class LRUCache:
    __slots__ = ('data', 'capacity')

    def __init__(self, capacity: int):
        self.data: Dict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        return -1 if key not in self.data else self.data.setdefault(key, self.data.pop(key))

    def put(self, key: int, value: int) -> None:
        try:
            self.data.move_to_end(key)
            self.data[key] = value
        except KeyError:
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)