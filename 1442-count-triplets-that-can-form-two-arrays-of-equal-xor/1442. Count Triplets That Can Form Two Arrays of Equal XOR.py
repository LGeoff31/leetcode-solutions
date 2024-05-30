class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarr = arr[i:j+1]
                acc = 0
                for num in subarr:
                    acc ^= num
                if acc == 0:
                    res += len(subarr) - 1
        return res