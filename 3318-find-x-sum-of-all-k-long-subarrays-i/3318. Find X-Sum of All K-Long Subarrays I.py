class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        def calc(subarr):
            dic = Counter(subarr)
            res = 0
            lst = sorted([(b,a) for a,b in dic.items()], reverse=True)
            for i in range(x):
                if i >= len(lst): break
                res += lst[i][0] * lst[i][1]
            return res
        for i in range(len(nums) - k+1):
            res.append(calc(nums[i:i+k]))
        return res