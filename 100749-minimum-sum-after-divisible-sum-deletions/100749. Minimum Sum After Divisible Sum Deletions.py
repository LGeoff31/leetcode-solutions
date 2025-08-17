class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        """
        dp? subsequence must have same remainder as sum % k
        prefix[i] % k = prefix[j] % k, j < i
        at index i, set dp[i] = max sum we can delete using first i values
        at each iteration we can
        1) not end up deleting anything dp[i] = dp[i-1]
        2) end up deleting, pref[i] - prefix[j] % k == 0, so we gain (prefix[i] - prefix[j]) + dp[j]
        
        preprocess rem[j]
        """
        if k == 1: return 0
        n = len(nums)
        total = sum(nums)
        best_so_far = [-1e20] * k
        best_so_far[0] = 0 
        prefix_acc = 0
        dp = [0] * n
        for i in range(len(nums)):
            prefix_acc += nums[i]
            r = prefix_acc % k
            # DELETE + NO DELETE
            a = prefix_acc + best_so_far[r]
            dp[i] = max(dp[i-1], a)

            b = dp[i] - prefix_acc
            if b > best_so_far[r]:
                best_so_far[r] = b
        return total - dp[-1] if total - dp[-1] < 1e19 else prefix_acc
                
            
        
        # dp = [1e9] * k
        # dp[0] = 0