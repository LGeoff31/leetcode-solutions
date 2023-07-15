class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        hour, minute = event1[0].split(':')
        hour = int(hour)
        minute = int(minute)
        event_1_start = hour + (minute/60)
        hour, minute = event1[1].split(':')
        hour = int(hour)
        minute = int(minute)
        event_1_end = hour + (minute/60)
        hour, minute = event2[0].split(':')
        hour = int(hour)
        minute = int(minute)
        event_2_start = hour + (minute/60)
        hour, minute = event2[1].split(':')
        hour = int(hour)
        minute = int(minute)
        event_2_end = hour + (minute/60)

        print(event_1_start, event_1_end)
        print(event_2_start, event_2_end)
        if event_1_start <= event_2_start <= event_1_end:
            return True
        if event_2_start <= event_1_start <= event_2_end:
            return True
        return False
