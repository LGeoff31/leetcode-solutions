class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = 1e9
        lst = sorted([(waterStartTime[i], waterDuration[i]) for i in range(len(waterStartTime))])
        waterStartTime = []
        waterDuration = []
        for x,y in lst:
            waterStartTime.append(x)
            waterDuration.append(y)
        print(waterStartTime)
        print(waterDuration)

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                if landStartTime[i] + landDuration[i] >= waterStartTime[j]:
                    res = min(res, landStartTime[i] + landDuration[i] + waterDuration[j])
                else:
                    res = min(res, waterStartTime[j] + waterDuration[j])

                if waterStartTime[j] + waterDuration[j] >= landStartTime[i]:
                    res = min(res, waterStartTime[j] + waterDuration[j] + landDuration[i])
                else:
                    res = min(res, landStartTime[i] + landDuration[i])
        return res