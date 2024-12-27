import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dic = defaultdict(list)
        for i, num in enumerate(self.nums):
            self.dic[num].append(i)
        

    def pick(self, target: int) -> int:
        indicies = self.dic[target]
        return random.choice(indicies)



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)