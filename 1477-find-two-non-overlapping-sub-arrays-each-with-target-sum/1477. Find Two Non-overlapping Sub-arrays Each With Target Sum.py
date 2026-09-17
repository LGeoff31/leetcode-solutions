class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # subarrays: sliding window
        # non overlapping is a bitch 
            # had to check discussion for hint about prefix/suffix
            # each prefix[i] and suffix[i] will be non-overlapping pairs

        prefix = [0] * len(arr)
        suffix = [0] * len(arr)

        # prefix
        l = 0
        r = 0
        r_sum = 0
        smallest = float('inf')

        while r < len(arr):
            r_sum += arr[r]
            while r_sum > target:
                r_sum -= arr[l]
                l += 1
            if r_sum == target:
                smallest = min(smallest, r - l + 1)
            prefix[r] = smallest
            r += 1
            # print(prefix)
        

        # suffix - just mirror prefix lol
        r = len(arr) - 1
        l = len(arr) - 1
        r_sum = 0
        smallest = float('inf')
        
        while l >= 0:
            r_sum += arr[l]
            while r_sum > target:
                r_sum -= arr[r]
                r -= 1
            if r_sum == target:
                smallest = min(smallest, r - l + 1)
            suffix[l] = smallest
            l -= 1
            # print(suffix)
        
        # bam
        res = float('inf')
        for i in range(len(arr) - 1):
            res = min(res, prefix[i] + suffix[i + 1])
        if res == float('inf'):
            return -1
        else:
            return res

        

        

