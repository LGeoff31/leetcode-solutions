class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i, n in enumerate(nums):
            dic[n].append(i)
        res = 1e9
        for num in dic:
            indicies = dic[num]
            for i in range(2, len(indicies)):
                a,b,c = indicies[i-2], indicies[i-1], indicies[i]
                res = min(res, c-b + b-a + c-a)
        return res if res != 1e9 else -1