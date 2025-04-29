class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp_s = [0] * (max(nums) + 2)
        dp_c = [0] * (max(nums) + 2)
        dp_s[nums[0]] = nums[0]
        dp_c[nums[0]] = 1
        # print(dp_s)
        # print(dp_c)
        # print()
        for num in nums[1:]:
            dp_s[num] += num*(1+dp_c[num+1]+dp_c[num-1])  + dp_s[num+1] + dp_s[num-1]
            dp_c[num] += dp_c[num+1] + dp_c[num-1] + 1
            # if dp_c[num+1] != 0:
            #     dp_s[num] += (num*(1+dp_c[num+1]) + dp_s[num+1])
            #     dp_c[num] += dp_c[num+1] + 1
            # if dp_c[num-1] != 0:
            #     dp_s[num] += (num*(1+dp_c[num-1]) + dp_s[num-1])
            #     dp_c[num] += dp_c[num-1] + 1
            # if dp_c[num+1] == 0 and dp_c[num-1] == 0:
            #     dp_s[num] += num
            #     dp_c[num] += 1

            # dp_c[num] += dp_c[num-1] + dp_c[num+1]
            # print(dp_s)
            # print(dp_c)
            # print()
        return sum(dp_s) % MOD