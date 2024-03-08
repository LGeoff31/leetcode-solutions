class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        res = []
        incr, dcr = [0], [0]
        for i in range(1, n):
            if security[i] > security[i - 1]:
                incr.append(incr[-1] + 1)
                dcr.append(0)
            elif security[i] < security[i - 1]:
                dcr.append(dcr[-1] + 1)
                incr.append(0)
            else:
                incr.append(incr[-1] + 1)
                dcr.append(dcr[-1] + 1)
        
        for i in range(time, n - time):
            if dcr[i] >= time and incr[i + time] >= time: res.append(i)

        return res