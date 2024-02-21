from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        idx = 0
        zeroCount = 0
        queue = deque([])
        if k == 0:
            count = 0
            res = 0 
            for i in range(len(nums)):
                if nums[i] == 1:
                    count += 1
                    res = max(res, count)
                else:
                    count = 0
            return res
        while idx < len(nums):
            if zeroCount < k or (zeroCount == k and nums[idx] == 1):
                queue.append(nums[idx])
                res = max(res, len(queue))
            else:
                elem = queue.popleft()
                if elem == 0: zeroCount -= 1
                queue.append(nums[idx])
            zeroCount += nums[idx] == 0
            idx += 1
            # print(queue)
        return res

       