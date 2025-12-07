class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        a = Counter(nums)
        for n in nums:
            if a[n] == 1 and n-1 not in a and n+1 not in a:
                res.append(n)
        return res