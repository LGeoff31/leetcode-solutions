class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        dic = defaultdict(int)
        # nums = list(set(nums))
        for n in nums:
            n %= value
            dic[n] += 1
        curr = 0
        print(dic)
        while True:
            if curr%value not in dic or dic[curr%value] <= curr // value: # curr = 11, value = 2. require 5 1's
                return curr
            curr += 1 
