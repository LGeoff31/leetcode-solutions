class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        total = start= 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0: 
                total = 0
                start = i + 1
        return start

            # valid = True
            # idx = i+1

            # while idx < len(gas) and valid:
            #     if total < 0: valid = False
            #     total += diff[idx]
            #     idx+=1
            # if valid: return i
