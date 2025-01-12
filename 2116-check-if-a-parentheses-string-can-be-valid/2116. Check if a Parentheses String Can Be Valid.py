class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1: return False
        # Swwep left to right
        free = 0
        locked_open = 0
        locked_closed = 0
        for i, c in enumerate(s):
            if locked[i] == "0":
                free += 1
            else:
                if s[i] == ")":
                    # Must be a closing one on the lefthand side, use locked_open otherwise use free
                    if locked_open > 0:
                        locked_open -= 1
                    elif free > 0:
                        free -= 1
                    else:
                        return False
                else:
                    locked_open += 1
        # Swwep right to left
        free = 0
        locked_open = 0
        locked_closed = 0
        for i in range(len(s) -1, -1, -1):
            if locked[i] == "0":
                free += 1
            else:
                if s[i] == "(":
                    # Must be a closing one on the lefthand side, use locked_open otherwise use free
                    if locked_closed > 0:
                        locked_closed -= 1
                    elif free > 0:
                        free -= 1
                    else:
                        return False
                else:
                    locked_closed += 1
        print(locked_open, locked_closed, free)
        return True