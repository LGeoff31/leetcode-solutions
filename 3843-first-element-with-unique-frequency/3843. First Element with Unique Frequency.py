class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        a = Counter(nums)
        lst = [(val, key) for key, val in a.items()]
        lst.sort()
        if len(lst) == 1:
            return lst[0][1]
        unique = set()
        if lst[0][0] != lst[1][0]:
            unique.add(lst[0][1])
        for i in range(1, len(lst)):
            if i + 1 < len(lst):
                if lst[i][0] != lst[i-1][0] and lst[i][0] != lst[i+1][0]:
                    unique.add(lst[i][1])
            else:
                if lst[i][0] != lst[i-1][0]:
                    unique.add(lst[i][1])
        for n in nums:
            if n in unique:
                return n
        return -1