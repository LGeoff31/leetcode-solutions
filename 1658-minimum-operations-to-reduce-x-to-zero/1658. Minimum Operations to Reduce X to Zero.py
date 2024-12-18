class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefix = list(accumulate(nums))
        suffix = list(accumulate(nums[::-1]))[::-1]
        print(prefix)
        print(suffix)

        dic1, dic2 = {}, {}
        for i, num in enumerate(prefix):
            dic1[num] = i
        for i, num in enumerate(suffix):
            dic2[num] = i
        res = 1e9
        # Includes at least one of prefixes
        for i in range(len(prefix)):
            remain = x - prefix[i]
            if remain in dic2:
                idx = dic2[remain]
                if idx <= i: continue
                # print(i, idx)
                res = min(res, (i+1) +  n - idx)
        # Only prefix
        for i in range(len(prefix)):
            if prefix[i] == x:
                res = min(res, i+1)
        # Only suffix
        for i in range(len(suffix)):
            if suffix[i] == x:
                res = min(res, n - i)
        return res if res != 1e9 else -1