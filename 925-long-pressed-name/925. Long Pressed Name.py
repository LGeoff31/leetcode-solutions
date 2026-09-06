class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if typed[j] == name[i-1] and i-1 >= 0:
                    j += 1
                else:
                    return False
        print(i, j)
        return i == len(name) and all(c==name[-1] for c in typed[j:])