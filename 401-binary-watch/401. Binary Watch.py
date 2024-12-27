from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:  # Max LEDs on a binary watch is 8 (4 for hours, 6 for minutes)
            return []
        
        res = []
        # Iterate over all possible hours and minutes
        for h in range(12):  # Hours range: 0-11
            for m in range(60):  # Minutes range: 0-59
                # Count the total LEDs that are turned on
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Format time as "H:MM"
                    res.append(f"{h}:{m:02d}")
        return res
