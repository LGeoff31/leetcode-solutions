class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        res = tasks[0][1]
        energy = res - tasks[0][0]
        for i in range(1, len(tasks)):
            if energy < tasks[i][1]:
                res += tasks[i][1] - energy
                energy = tasks[i][1] - tasks[i][0]
            else:
                energy -= tasks[i][0]
        return res
        """
        12+9+8+3+1 = 33
        """