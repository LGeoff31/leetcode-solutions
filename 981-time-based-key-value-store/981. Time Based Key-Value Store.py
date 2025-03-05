class TimeMap:
    def __init__(self):
        self.dic = defaultdict(list) # {foo: [(1, bar)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.dic[key], [timestamp, "zzzzzzzzzz" * 10]) - 1
        if idx < 0: return ""

        return self.dic[key][idx][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)