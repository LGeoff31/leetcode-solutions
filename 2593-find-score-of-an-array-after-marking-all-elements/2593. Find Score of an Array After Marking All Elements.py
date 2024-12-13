class Solution:
    def findScore(self, nums: List[int]) -> int:
        lst = [[num, i] for i, num in enumerate(nums)]
        lst = sorted(lst, key=lambda x: (x[0], x[1]))
        visited = set()

        idx = 0
        res = 0
        
        while idx < len(nums):
            num, i = lst[idx]
            if i not in visited:
                visited.add(i)
                visited.add(i+1)
                visited.add(i-1)
                res += num
            idx += 1

        return res