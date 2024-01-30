class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        count = 0
        acc = 0
        prefixSum = []
        for num in nums:
            acc += num
            prefixSum.append(acc)
        for i in range(len(nums)):
            if prefixSum[i] - k in dic:
                count += dic[prefixSum[i] - k]
                dic[prefixSum[i]] = 1 + dic.get(prefixSum[i], 0)
            else:
                dic[prefixSum[i]] = 1 + dic.get(prefixSum[i], 0)
        return count
