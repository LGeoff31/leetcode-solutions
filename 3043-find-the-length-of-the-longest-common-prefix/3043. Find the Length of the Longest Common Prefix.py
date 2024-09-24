class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        a = set()
        for i in range(len(arr1)):
            for j in range(1, 1 + len(str(arr1[i]))):
                a.add(str(arr1[i])[:j])
        res = 0
        for i in range(len(arr2)):
            for j in range(1, 1 + len(str(arr2[i]))):
                if str(arr2[i])[:j] in a:
                    res = max(res, j)
        return res