class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        lst = []
        idx = 0
        while idx < len(nums):
            start_idx = idx
            while idx+1 < len(nums) and nums[idx] % 2 != nums[idx+1] % 2: # Different parity
                idx += 1
            lst.append((start_idx, idx))
            idx += 1
        res = []
        for start_q, end_q in queries:
            if start_q == end_q:
                res.append(True)
                continue
            idx = bisect_left(lst, (start_q, 0))  # Binary search for the query start
            print(idx)
            # Check if the found interval completely covers the query
            if idx-1 >= 0 and lst[idx-1][0] <= start_q and lst[idx-1][1] >= end_q:
                res.append(True)
                continue
            
            if idx < len(lst) and lst[idx][0] <= start_q and lst[idx][1] >= end_q:
                res.append(True)
            else:
                res.append(False)
        print(lst)
        return res