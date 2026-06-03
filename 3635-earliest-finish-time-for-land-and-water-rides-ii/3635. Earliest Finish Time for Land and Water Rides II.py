class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def solve(aTime, aDuration, bTime, bDuration):
            earliest_end_a_start, earliest_end_a_end = float("inf"), float("inf")

            for start, duration in zip(aTime, aDuration):
                if start + duration < earliest_end_a_end:
                    earliest_end_a_start = start
                    earliest_end_a_end = start + duration
            
            result = float("inf")
            for start, duration in zip(bTime, bDuration):
                start = max(start, earliest_end_a_end)

                result = min(result, start + duration)

            return result
        
        return min(solve(landStartTime, landDuration, waterStartTime, waterDuration), solve(waterStartTime, waterDuration, landStartTime, landDuration))
        