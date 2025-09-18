from sortedcontainers import SortedList
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        # Initialize a heap: (priority, taskId, userId)
        self.lst = SortedList()
        self.dic = {}
        for userId, taskId, priority in tasks:
            self.dic[taskId] = [userId, priority]
            self.lst.add((priority, taskId, userId))
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.dic[taskId] = [userId, priority]     
        self.lst.add((priority, taskId, userId))

    def modifiedBinarySearch(self, priority, taskId, userId):
        # DOUUBLE BS
        l, r = 0, len(self.lst) - 1
        while l <= r:
            mid = (l + r) // 2
            p, t, u = self.lst[mid]
            if p == priority:
                # Now binary search for taskId = t
                if t == taskId:
                    return mid
                elif t < taskId:
                    l = mid + 1
                else:
                    r = mid - 1
            elif p < priority:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.dic[taskId]
        self.dic[taskId] = [userId, newPriority]
        # Find i, self.lst[i] = (priority, taskId, userId)
        l, r = 0, len(self.lst) - 1
        idx = self.modifiedBinarySearch(priority, taskId, userId)
        self.lst.remove(self.lst[idx])
        self.lst.add((newPriority, taskId, userId))

    def rmv(self, taskId: int) -> None:
        userId, priority = self.dic[taskId]
        del self.dic[taskId]
        idx = self.modifiedBinarySearch(priority, taskId, userId)
        self.lst.remove(self.lst[idx])

    def execTop(self) -> int:
        if len(self.dic) == 0:
            return -1
        p, t, u = self.lst[-1]
        self.rmv(t)
        return u

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()