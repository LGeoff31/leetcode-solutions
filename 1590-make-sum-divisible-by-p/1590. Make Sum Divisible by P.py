class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dic = defaultdict(list)
        dic[0].append(-1)
        prefix = list(accumulate(nums))
        target_sum = sum(nums)
        res = len(nums)
        rem = target_sum % p
        if rem == 0: return 0

        for i in range(len(nums)):
            curr = prefix[i] % p
            target = (curr - rem + p) % p
            if target in dic:
                res = min(res, i - dic[target][-1])
            dic[curr].append(i)
           
        return res if res < len(nums)  else -1


# [3,1,4,2], p=6
# total_sum = 10
# {3: 0, 4: 1, 2: 2, }