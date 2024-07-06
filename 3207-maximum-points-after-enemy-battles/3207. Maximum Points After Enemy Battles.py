class Solution:
    def maximumPoints(self, lst: List[int], energy: int) -> int:
        if energy < min(lst):
            return 0
        lst.sort()
        energy -= lst[0] # Have 1 point now
        energy += sum(lst)
        return energy // lst[0]


