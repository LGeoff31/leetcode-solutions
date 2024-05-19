class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        z=sum(nums)
        delta = []

        for n in nums:
            delta.append((n^k) - n)
        delta.sort()
        res=0
        print(delta)
        for i in range(len(delta)-1, 0, -2):
            if delta[i] + delta[i-1] >= 0:
                res += delta[i] + delta[i-1]

            print(i)
        

        return res + z
        
        