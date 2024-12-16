class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # The subarray must have sum of 0 or 1
        for i in range(len(nums)):
            if nums[i] < k:
                nums[i] = -1
            elif nums[i] > k:
                nums[i] = 1
            else:
                nums[i] = 0
        res = 0
        dic = defaultdict(list) # val: [idx]
        prefix = list(accumulate(nums))
        idx_zero = nums.index(0)
        dic[0] = [-1]
        for i in range(len(prefix)): #O(n)
            if idx_zero > i: 
                dic[prefix[i]].append(i)
                continue
            if prefix[i] in dic or prefix[i]-1 in dic:
                indexes_sum_0 = dic[prefix[i]]
                indexes_sum_1 = dic[prefix[i] - 1]
                res += bisect_left(indexes_sum_0, idx_zero)
                res += bisect_left(indexes_sum_1, idx_zero)
           
            dic[prefix[i]].append(i)

        return res