class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n+1)
        gaps[0] = startTime[0]
        gaps[n] = eventTime - endTime[-1]
        
        # Popualte gaps
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i-1]

        prefix = list(accumulate(gaps))
        print(prefix)
        res = 0
        for i in range(k, n+1):
            print('reached')
            if i-k == 0:
                res = max(res, prefix[i])
            else:
                res = max(res, prefix[i] - prefix[i-k-1])
        return res