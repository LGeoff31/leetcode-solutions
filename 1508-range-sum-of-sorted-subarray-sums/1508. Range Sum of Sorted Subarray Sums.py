class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        lst = []
        prefix = [0] + list(accumulate(nums))
        for i in range(len(prefix)):
            for j in range(i+1, len(prefix)):
                lst.append(prefix[j] - prefix[i])
        lst.sort()

        return sum(lst[left-1:right]) % MOD