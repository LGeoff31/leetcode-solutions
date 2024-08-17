class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = [-1] * (n - k + 1)
        queue = deque()
        dp = [0] * n

        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 0
        for i in range(n):
            while queue and queue[0] < i - k + 1:
                queue.popleft()
            while queue and nums[queue[-1] <= nums[i]]:
                queue.pop()
            queue.append(i)

            if i >= k - 1:
                start = i - k + 1
                if dp[i] >= k - 1:
                    results[i-k+1] = nums[queue[0]]
                else:
                    results[i-k+1] = -1
        
        
        return results