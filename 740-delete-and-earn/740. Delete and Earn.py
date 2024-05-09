class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        #[2,2,3,3,3,4,5]
        #[2,4,4,6,9,9,14]
        res = 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dic = Counter(nums)

        hashmap = defaultdict(list)
        hashmap[nums[0]].append(0)
        for i in range(1, len(nums)):
            if nums[i] - 1 in hashmap:
                idx = hashmap[nums[i] - 1][0] - 1
                if idx >= 0:
                    dp[i] = max(dp[i-1], nums[i] * dic[nums[i]] + dp[idx])
                else:
                    dp[i] = max(dp[i-1], nums[i] * dic[nums[i]])

            else:
                dp[i] = dp[i-1] + nums[i]
            hashmap[nums[i]].append(i)
        print(hashmap)
        print(dp)
        return max(dp)
            