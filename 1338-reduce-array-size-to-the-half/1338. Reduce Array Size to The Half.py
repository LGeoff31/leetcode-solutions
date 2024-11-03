class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        a = Counter(arr)
        lst = []
        for val in a.values():
            lst.append(val)
        lst.sort(reverse=True)
        total = len(arr)
        res = 0
        num = 0
        idx = 0
        while num < total // 2:
            num += lst[idx]
            idx += 1
            res += 1
        return res