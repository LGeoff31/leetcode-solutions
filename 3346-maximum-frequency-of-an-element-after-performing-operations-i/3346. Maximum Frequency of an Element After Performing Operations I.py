class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        lst = [0] * max(nums)
        for n in nums:
            lst[n-1] += 1    
        prefix = list(accumulate(lst))
        print(prefix)
        res = 0

        for i in range(len(prefix)):
            if i-k-1 >= 0:
                res = max(res, min(prefix[min(i+k, len(prefix)-1)] - prefix[i-k-1] - lst[i], numOperations) + lst[i])
            else:
                res = max(res, min(prefix[min(i+k, len(prefix)-1)] - lst[i], numOperations) + lst[i])
        return max(res, max(Counter(nums).values()))
