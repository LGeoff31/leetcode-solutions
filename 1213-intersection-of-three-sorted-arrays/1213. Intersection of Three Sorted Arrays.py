class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        a, b = set(arr1), set(arr2)
        for num in arr3:
            if num in a and num in b:
                res.append(num)
        return res