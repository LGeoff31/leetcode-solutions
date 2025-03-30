class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        j = 0
        count = 0
        if sum(c not in source for c in target) > 0: return -1
        while j < len(target):
            i = 0
            while j < len(target) and i < len(source):
                if target[j] == source[i]:
                    j += 1
                i += 1

            count += 1
            print(i, j)
        return count