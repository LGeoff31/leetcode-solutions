class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic = defaultdict(list)
        for i, n in enumerate(nums):
            dic[n].append(i)

        def is_contigious(lst):
            for i in range(1, len(lst)):
                if lst[i] != lst[i-1] + 1:
                    return False 
            return True
        res = 0
        for key in dic:
            res += is_contigious(dic[key])
        return res