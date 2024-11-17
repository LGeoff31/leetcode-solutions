class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int: 
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        queue = deque()
        res = 1e9

        for i in range(n+1):
            while queue and prefix[i] - prefix[queue[0]] >= k:
                # Valid
                res = min(res, i - queue.popleft())
            while queue and prefix[i] <= prefix[queue[-1]]:
                queue.pop()
            queue.append(i)
        return res if res != 1e9 else -1