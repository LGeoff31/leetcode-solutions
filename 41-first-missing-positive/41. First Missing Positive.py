class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:   
        lst = [num for num in nums if num > 0]
        print(lst)
        for i in range(len(lst)):
            idx = abs(lst[i]) - 1
            if idx < len(lst) and lst[idx] > 0:
                lst[idx] *= -1
        for i in range(len(lst)):
            if lst[i] > 0:
                return i + 1
        return len(lst) + 1
        