class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 +7
        nums.sort()
        res = 0
        initial = 1
        # Do maximums
        for i in range(len(nums)):
            remaining_elements_left = i
            res += initial * nums[i]
            initial = 2 * initial - comb(i, k-1)


            # for j in range(k):
            #     res += comb(remaining_elements_left, j) * nums[i]
        initial = 1
        nums.sort(reverse=True)
        for i in range(len(nums)):
            remianing_elements_left = i
            res += initial * nums[i]
            initial = 2 * initial - comb(i, k-1)
            # for j in range(k):
            #     res += comb(remianing_elements_left, j) * nums[i]
        print(res)
        return res % MOD

