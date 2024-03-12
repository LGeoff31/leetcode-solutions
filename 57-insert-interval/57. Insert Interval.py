class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not len(intervals):
            return [newInterval]
        #check goes very end
        if intervals[-1][1] < newInterval[0]:
            res = []
            for interval in intervals:
                res.append(interval)
            res.append(newInterval)
            return res

        #check goes very beggining
        if intervals[0][0] > newInterval[1]:
            res = [newInterval]
            for interval in intervals:
                res.append(interval)
            return res

        res = []
        idx = 0
        while idx < len(intervals):
            #check overlap
            if intervals[idx][0] <= newInterval[1] <= intervals[idx][1] or newInterval[0] <= intervals[idx][1] <= newInterval[1]:
                new_lst = intervals[idx]
                while idx < len(intervals) and (intervals[idx][0] <= newInterval[1] <= intervals[idx][1] or newInterval[0] <= intervals[idx][1] <= newInterval[1]):
                    new_lst[0] = min(newInterval[0], new_lst[0])
                    new_lst[1] = max(newInterval[1], intervals[idx][1])
                    idx += 1
                idx -= 1
                res.append(new_lst)
            else:
            #check no overlap
            #can be placed somewhere in middle
                if idx+1 < len(intervals) and intervals[idx][1] < newInterval[0] < intervals[idx+1][0] and intervals[idx][1] < newInterval[1] < intervals[idx+1][0] :
                    res.append(intervals[idx])
                    res.append(newInterval)
                else:
                    res.append(intervals[idx])
            idx += 1
        return res


        