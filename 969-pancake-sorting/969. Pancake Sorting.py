class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        a = sorted(arr)
        j = len(a) - 1
        for i in range(n-1, -1, -1): # n-1 -> 0
            idx = arr.index(a[j])
            # Flips it to the front
            res.append(idx+1)
            arr[:idx+1] = arr[:idx+1][::-1]
            # Flips it to the right position 
            res.append(i+1)
            arr[:i+1] = arr[:i+1][::-1]
            j -= 1

        return res