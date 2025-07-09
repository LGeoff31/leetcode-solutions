class Solution:
    def maxFreeTime(self, eventTime: int, maxShifts: int, startTimes: List[int], endTimes: List[int]) -> int:

        # print(empty_end)
        # print(gaps)
        
        # if not gaps: return 0
        # idx = 0
        # currSum = 0
        # for i in range(k + 1):
        #     if i < len(empty_end):
        #         currSum += empty_end[i] - empty_start[i]
        # l = 0
        # idx = i + 1
        # res = max(res, currSum)
        # while idx < len(empty_end):
        #     currSum -= empty_end[l] - empty_start[l]
        #     currSum += empty_end[idx] - empty_start[idx]
        #     res = max(res, currSum)
        #     l += 1
        #     idx += 1
        # return res
        numMeetings = len(startTimes)
        meetingDurations = [endTimes[i] - startTimes[i] for i in range(numMeetings)]

        cumulativeDurations = [0] * (numMeetings + 1)
        for i in range(numMeetings):
            cumulativeDurations[i + 1] = cumulativeDurations[i] + meetingDurations[i]

        totalMeetingTime = cumulativeDurations[numMeetings]

        if maxShifts >= numMeetings:
            return max(0, eventTime - totalMeetingTime)

        maxIdleTime = 0

        for i in range(numMeetings):
            if i <= maxShifts:
                freeSlot = startTimes[i] - cumulativeDurations[i]
                maxIdleTime = max(maxIdleTime, freeSlot)

        for j in range(numMeetings - 1, -1, -1):
            if (numMeetings - 1 - j) <= maxShifts:
                freeSlot = eventTime - (endTimes[j] + (totalMeetingTime - cumulativeDurations[j + 1]))
                maxIdleTime = max(maxIdleTime, freeSlot)

        movingWindow = deque()

        for j in range(1, numMeetings):
            minIndex = max(0, j - maxShifts - 1)

            while movingWindow and movingWindow[0] < minIndex:
                movingWindow.popleft()

            prevIndex = j - 1
            currentDiff = cumulativeDurations[prevIndex + 1] - endTimes[prevIndex]

            while movingWindow:
                lastIndex = movingWindow[-1]
                lastValue = cumulativeDurations[lastIndex + 1] - endTimes[lastIndex]

                if lastValue <= currentDiff:
                    movingWindow.pop()
                else:
                    break

            movingWindow.append(prevIndex)

            bestGap = cumulativeDurations[movingWindow[0] + 1] - endTimes[movingWindow[0]]
            potentialIdleTime = startTimes[j] - cumulativeDurations[j] + bestGap

            maxIdleTime = max(maxIdleTime, potentialIdleTime)

        return max(0, maxIdleTime)
        # print(
            
        # idx = 0
        # while idx < len(empty_start):
        #     # Try to extend r to combine as many unfilled gaps
        #     unwanted = 0
        #     space = 0
        #     while idx < len(empty_start):
        #         if idx != 0:
        #             unwanted += (empty_end[idx] - empty_start[idx-1]) - (empty_end[idx]-empty_start[idx] + empty_end[idx-1]-empty_start[idx-1])
        #         if bisect_left(gaps, unwanted) == len(gaps): # No place put it
        #             break
        #         space += empty_ned[idx] - empty_start[idx]
        #         gaps.remove(empty_end[idx] - empty_start[idx])
        #         res = max(res, space)
        #         idx += 1        
        

        # return 0
        
        