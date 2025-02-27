class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        nums = set(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                curr = 2
                prev1 = arr[i]
                prev2 = arr[j]

                while prev1 + prev2 in nums:
                    curr += 1
                    tmp = prev1
                    prev1 = prev2
                    prev2 = tmp + prev2

                res = max(res, curr)
        return res if res > 2 else 0