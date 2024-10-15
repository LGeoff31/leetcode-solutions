class Solution:

    def __init__(self, w: List[int]):
        self.prefix = list(accumulate(w))
        print(self.prefix)
        

    def pickIndex(self) -> int:
        random_num = randint(1, self.prefix[-1])
        low, high = 0, len(self.prefix)
        while low < high:
            mid = low + (high - low) // 2
            if self.prefix[mid] < random_num:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()