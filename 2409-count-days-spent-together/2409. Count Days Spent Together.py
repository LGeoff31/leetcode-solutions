from datetime import date

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:
        def parse(s):
            month, day = map(int, s.split('-'))
            return date(2021, month, day)

        start = max(parse(arriveAlice), parse(arriveBob))
        end = min(parse(leaveAlice), parse(leaveBob))

        return max(0, (end - start).days + 1)