class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            j = bisect_right(nums, target-nums[i])-1
            if i == j and 2*nums[i] > target: continue
            gap = j-i
            if gap >= 0:
                res += max(2**(gap),0)
            # print(i, j)
            # for k in range(2, gap+1):
            #     res += max(0,comb(gap, k))
            # res += max(0,gap+1)

        return res % MOD