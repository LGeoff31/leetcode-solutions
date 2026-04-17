class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x):
            ans=0
            while x>0:
                x, d=divmod(x, 10)
                ans=10*ans+d
            return ans
        mp={}
        dist=inf
        for i, x in enumerate(nums):
            R=rev(x)
            if x in mp:
                dist=min(dist, i-mp[x])
            mp[R]=i
        return -1 if dist==inf else dist
        