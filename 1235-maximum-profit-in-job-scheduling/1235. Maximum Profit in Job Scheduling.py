class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache={}


        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            #dont include element at index i
            res = dfs(i+1)
            #incldue element at index i  
            j = bisect.bisect(intervals, (intervals[i][1],-1,-1))
            cache[i] = res = max(res,intervals[i][2] + dfs(j))
            return res      
        
        return dfs(0)