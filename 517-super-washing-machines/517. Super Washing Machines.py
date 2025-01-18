class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines) % len(machines) != 0: return -1
        avg = sum(machines) // len(machines)
        for i in range(len(machines)):
            machines[i] = machines[i] - avg
        giveouts = 0
        res = 0
        currSum = 0
        for i in range(len(machines)):
            currSum += machines[i]
            res = max(res, abs(currSum), machines[i])

        print(machines)
        return res