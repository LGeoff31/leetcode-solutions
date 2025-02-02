class Solution:
    def check(self, nums: List[int]) -> bool:
        lst = deque(nums)
        n = len(nums)
        for i in range(n):
            if lst == deque(sorted(lst)):
                return True
            lst.append(lst.popleft())
            print(lst, sorted(lst), lst == sorted(lst))
        return False