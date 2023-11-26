class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        prefix_sum = []
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            prefix_sum.append(curr)

        def calc_prefix_before(idx):
            if idx != 0:
                return -1 * prefix_sum[idx-1]
            return 0

        def calc_prefix_after(idx):
            return prefix_sum[-1] - prefix_sum[idx]

        for i in range(len(nums)):
            elements_before = i
            elements_after = len(nums) - (i+1)
            a = nums[i] * (elements_before - elements_after)
            b = calc_prefix_before(i)
            c = calc_prefix_after(i)
            res = a + b + c

            result.append(res)
        return result
