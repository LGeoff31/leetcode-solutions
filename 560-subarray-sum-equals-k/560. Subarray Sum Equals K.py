class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums))
        dic = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            currSum = prefix[i]
            if currSum == k:
                res += 1

            target = k - currSum
            if target in dic:
                res += dic[target]
            dic[-currSum] += 1
        return res

