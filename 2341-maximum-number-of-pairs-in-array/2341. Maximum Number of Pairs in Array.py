class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        res = [0, 0]
        for key in a:
            res[0] += a[key] // 2
            a[key] = a[key] % 2
        b = 0
        for key in a:
            if a[key]:
                b += 1
        res[1] = b
        return res
        
