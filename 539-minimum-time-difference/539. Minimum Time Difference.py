class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort(key = lambda x: (int(x.split(":")[0]), int(x.split(":")[1])))
        print(timePoints)
        def calc_diff(time1, time2):
            """
            time1 = 13:50
            time2 = 14:34

            diff_min = -16
            diff_h = 1 -> (60 minutes)
            60 - 16 = 44

            HOW MANY MINUTES ARE THERE ON 24-HOUR CLOCK??
            24x60 = 1440

            """
            h1, m1 = [int(x) for x in time1.split(":")]
            h2, m2 = [int(x) for x in time2.split(":")]

            if h1 > h2 or (h1 == h2 and m1 > m2):
                return calc_diff(time2, time1)
            print(time2, time1)
            # Enforced time2 > time1
            res = (m2 - m1) + (h2-h1) * 60
            return min(res, 1440 - res)

        minimum_time_difference = float('inf')
        for i in range(1, len(timePoints)):
            minimum_time_difference = min(minimum_time_difference, calc_diff(timePoints[i-1], timePoints[i]))

        minimum_time_difference = min(minimum_time_difference, calc_diff(timePoints[0], timePoints[-1]))
        return minimum_time_difference