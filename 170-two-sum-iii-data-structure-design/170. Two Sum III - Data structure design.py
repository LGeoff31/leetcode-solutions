from sortedcontainers import SortedList
class TwoSum:
    def __init__(self):
        self.lst = SortedList()
        

    def add(self, number: int) -> None:
        self.lst.add(number)

    def find(self, value: int) -> bool:
        l,r = 0, len(self.lst) - 1
        while l < r:
            total_sum = self.lst[l] + self.lst[r]
            if total_sum == value:
                return True
            elif total_sum > value: 
                r -= 1
            else:
                l += 1


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)