class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        subsequences = lambda arr: list(chain(*[combinations(arr, r) for r in range(len(arr)+1)]))
        lst = subsequences(nums)
        res = 0
        for arr in lst[1:]:
            z = set(arr)
            valid = True
            for i in arr:
                if i+k in z or i-k in z:
                    valid=False
            if valid: res+=1

        return res