class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # Doing tasks from smallest -> largest
        workers.sort()
        tasks.sort()
        print(workers)
        print(tasks)
        n = len(workers)

        def valid(mid):
            pills_left = pills
            lst = SortedList(workers[len(workers) - mid : ])
            for i in range(mid-1, -1, -1):
                if lst[-1] >= tasks[i]:
                    lst.pop()
                else:
                    if pills_left <= 0: return False
                    idx = bisect_left(lst, tasks[i] - strength)
                    if idx == len(lst):
                        return False
                    pills_left -= 1
                    lst.remove(lst[idx])
          
            return True

        l, r = 0, min(len(tasks), len(workers))
        res = 0
        while l <= r:
            mid = (l+r) // 2
            if mid == 0:
                res = mid
                l = mid + 1
                continue
            print('trying', mid)
            if valid(mid):
                print('got', mid)
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        
        return res