class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # Why not MOD all numbers by k????
        for i in range(len(nums)):
            nums[i] = nums[i] % k
        
        # Dp[i] = max length of subsequence with last element x such that x % k == i
        # (CurrNum + prevNum) % k == mod -> (prevNum + k - CurrNum) % k
        
        n = len(nums)
        dp = [[0] * k for _ in range(k)]

        for num in nums:
            currNum = num % k
            for mod in range(k):
                prevNum = (mod - currNum + k)%k
                dp[currNum][mod] = max(dp[currNum][mod], 1 + dp[prevNum][mod])
        res = 0
        for arr in dp:
            res = max(res, max(arr))
        return res