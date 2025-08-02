class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Each element must appear even amount times, then answer is findable
        """
        dic = defaultdict(int)
        for num in basket1:
            dic[num] += 1
        for num in basket2:
            dic[num] += 1
        print(dic)
        for key in dic:
            if dic[key] % 2 == 1:
                return -1
        
        goal = []
        for key in dic:
            for i in range(dic[key] // 2):
                goal.append(key)
        g = Counter(goal)
        a = Counter(basket1)
        b = Counter(basket2)
        basket1.sort()
        basket2.sort()
        print(basket1)
        print(basket2)
        # greedy take smallest and swap with largest
        res = 0
        extra1 = []
        extra2 = []
        for key in set(basket1):
            r = a[key] - g[key]
            if r > 0:
                for k in range(r):
                    extra1.append(key)
        for key in set(basket2):
            r = b[key] - g[key]
            if r > 0:
                for k in range(r):
                    extra2.append(key)
        extra1.sort()
        extra2.sort()
        print(extra1)
        print(extra2)
        i, j = 0, len(extra2) - 1
        while i < len(extra1):
            res += min(extra1[i], extra2[j])
            i += 1
            j -= 1
        res = 0
        global_min = min(min(basket1), min(basket2))
        for i in range(len(extra1)):
            res += min(min(extra1[i], extra2[len(extra2)-i-1]), 2*global_min)
        return res
        