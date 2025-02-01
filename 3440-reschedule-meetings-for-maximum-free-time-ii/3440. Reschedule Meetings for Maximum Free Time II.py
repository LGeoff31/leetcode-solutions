class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        start = []
        end = []

        for i in range(n):
            if i == 0:
                if startTime[i] != 0:
                    start.append(0)
                    end.append(startTime[i])
            else:
                start.append(endTime[i-1])
                end.append(startTime[i])
        if endTime[-1] != eventTime:
            start.append(endTime[-1])
            end.append(eventTime)
        gaps = SortedList()
        for i in range(len(start)):
            gaps.add(end[i] - start[i])
        res = 0
        idx = 0
        for i in range(n):
            addtemp1 = False
            addtemp2 = False
            # Try to see if ith block can be removed
            if startTime[i] == 0:
                # Only have gap to the right
                if idx < len(gaps):
                    if i+1 < len(startTime): 
                        temp1 = startTime[i+1] - endTime[i]
                    else:
                        temp1 = eventTime - endTime[i]
                    addtemp1 = True
                    gaps.remove(temp1)
                if gaps and bisect_left(gaps, endTime[i] - startTime[i]) != len(gaps):
                    # There is space
                    if i+1 < len(startTime) and i-1 >= 0: res = max(res, startTime[i+1] - endTime[i-1])
                    # Only after
                    elif i+1 < len(startTime): res = max(res, startTime[i+1])
                    # Only before
                    else: res = max(res, eventTime - endTime[i-1])
                    # print('reached', i, res)
                if addtemp1: gaps.add(temp1)
                # print(gaps)
            else:
                if idx+1 < len(gaps):
                    # temp1 = gaps[idx]
                    # temp2 = gaps[idx+1]
                    addtemp2 = True
                    addtemp1 = True
                    if i-1 >= 0 and i+1 < len(startTime):
                        temp1 = startTime[i] - endTime[i-1]
                        temp2 = startTime[i+1] - endTime[i]
                        gaps.remove(startTime[i] - endTime[i-1])
                        gaps.remove(startTime[i+1] - endTime[i])
                    elif i+1 < len(startTime):
                        temp1 = startTime[i+1] - endTime[i]
                        temp2 = startTime[i]
                        gaps.remove(startTime[i+1] - endTime[i])
                        gaps.remove(startTime[i])
                    else:
                        temp1 = startTime[i] - endTime[i-1]
                        temp2 = eventTime - endTime[i]
                        gaps.remove(startTime[i] - endTime[i-1])
                        gaps.remove(eventTime - endTime[i])
                elif idx < len(gaps):
                    temp1=gaps[idx]
                    addtemp1 = True
                    gaps.remove(temp1)
                # print('gaps', gaps)
                if gaps and bisect_left(gaps, endTime[i] - startTime[i]) != len(gaps):
                    # print('reached', i, gaps)
                    # Check if there previous
                    if i-1 >= 0 and i+1 < len(startTime):
                        res = max(res, startTime[i+1] - endTime[i-1])
                    # Only after
                    elif i+1 < len(startTime):
                        res = max(res, startTime[i+1])
                    # Only before
                    else:
                        res = max(res, eventTime - endTime[i-1])
                if addtemp1: gaps.add(temp1)
                if addtemp2: gaps.add(temp2)
                idx += 1
        print(res)
        res2 = 0
        for i in range(1, len(start)):
            res2 = max(res2, end[i]-start[i] + end[i-1]-start[i-1])
        return max(res, res2)
        