class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return []
        a = arr.copy()
        a.sort()
        dic = {a[0]: 1}
        prevNum = a[0]
        rank = 2
        i = 1
        while i < len(a):
            while i < len(a) and a[i] == prevNum:
                i += 1
            if i == len(a): break
            prevNum = a[i]
            dic[a[i]] = rank
            i += 1
            rank += 1
        res = []
        print(dic)
        print(arr)
        for i in arr:
            res.append(dic[i])
        return res
                