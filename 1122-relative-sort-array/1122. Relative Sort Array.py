class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a,b=Counter(arr1),Counter(arr2)
        res = []
        for key in arr2:
            res += [key] * a[key]
        c = []
        for i in range(len(arr1)):
            if arr1[i] not in b:
                c.append(arr1[i])

        return res + sorted(c)
        