class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]: 
        res = []
        for n in nums:
            if n < pivot:
                res.append(n)
        
        for n in nums:
            if n == pivot:
                res.append(n)

        for n in nums:
            if n > pivot:
                res.append(n)
        return res