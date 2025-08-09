class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i, arr in enumerate(mat):
            a = set(arr)
            for key in a:
                dic[key].append(i)
        res = 1e9
        for key in dic:
            if len(dic[key]) == len(mat):
                res = min(res, key)
        return res if res != 1e9 else -1