class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        res = -1e9
        tasks.sort(reverse=True)
        idx = 0
        i = 0
        processorTime.sort()
        print(tasks)
        while i < len(tasks) - 3:
            time = 0
            a = tasks[i:i+4]
            print(a)
            time = max(processorTime[idx]+a[0], processorTime[idx]+a[1], processorTime[idx]+a[2], processorTime[idx]+a[3])
            idx+=1
            res = max(time, res)
            print("res", res)
            i+=4
        return res        