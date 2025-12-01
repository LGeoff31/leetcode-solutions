class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_deg = (hour%12) * 30 + 30 * (minutes / 60)
        min_deg = 360 * (minutes / 60)
        print(hour_deg, min_deg)
        diff = abs(hour_deg - min_deg)
        return min(diff, 360-diff) 