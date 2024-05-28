class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        dic = defaultdict(list)
        for i in range(len(efficiency)):
            dic[efficiency[i]].append(i)

        efficiency.sort(reverse=True)
        a = sorted(list(set(efficiency)), reverse=True)
        s = []
        for num in a:
            for idx in dic[num]:
                s.append(speed[idx])
        print(efficiency)
        print(s)

        minHeap = []
        res = 0
        sumHeap = 0
        for i in range(len(s)):
            num_pop = 1 + len(minHeap) - k
            if num_pop <= 0:
                num_pop = 0

            for j in range(num_pop): #heap will have at most k elements
                if minHeap:
                    sumHeap -= heapq.heappop(minHeap)
                else:
                    break
            res = max(res, efficiency[i] * (s[i] + sumHeap))
            heapq.heappush(minHeap, s[i])
            sumHeap += s[i]
        return res % MOD



