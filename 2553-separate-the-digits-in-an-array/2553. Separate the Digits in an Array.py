class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for x in nums:
            t=[]
            while x>0:
                t.insert(0,x%10)
                x=x//10
            res+=t
        return res