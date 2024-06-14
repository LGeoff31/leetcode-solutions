class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #put all numbers 
        median = sorted(nums)
        res = [0] * len(nums)
        idx = 0
        #fill odd indicies with less median
        for i in range(1, len(nums), 2):
            res[i] = median[idx]
            idx += 1
        
        #fill even indicies
        for i in range(0, len(nums), 2):
            res[i] = median[idx]
            idx += 1
        return res

        