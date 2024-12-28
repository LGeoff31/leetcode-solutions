class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        lst = []
        curr = sum(nums[:k])
        lst.append(curr)
        
        for i in range(1, len(nums) - k + 1):
            curr += nums[i + k - 1] - nums[i - 1]
            lst.append(curr)
        print(lst)
        # dp[0] = lst[0]
        self.globalMax = 0
        self.res = []
        # print(lst)
        @cache
        def dfs(idx, taken):
            if taken == 3:
                return 0, []
                
            if idx >= len(lst):
                return -1e9, []

            # TAKE
            take_sum, take_indicies = dfs(idx+k, taken + 1)
            take_sum += lst[idx]
            # DONT TAKE
            skip_sum, skip_indicies = dfs(idx+1, taken)
            
            if take_sum > skip_sum:
                return take_sum, [idx] + take_indicies
            elif take_sum == skip_sum:
                return take_sum, min([idx] + take_indicies, skip_indicies)
            else:
                return skip_sum, skip_indicies
        _, res = dfs(0, 0)
        return res