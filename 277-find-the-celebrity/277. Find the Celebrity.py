# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Exists celebrity
        for i in range(n):
            # Assume i is celebrity
            valid = True
            for j in range(n):
                if j != i:
                    if not knows(j, i):
                        valid = False 
                        break
                    if knows(i, j):
                        valid = False
                        break
            if valid:
                return i
        return -1