class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        freq = Counter(arr)
        if difference == 0:
            return max(freq.values())
        cache = {}
        dic = defaultdict(list)

        def calc(idx):
            if idx in cache:
                return cache[idx]
            print("hello")
            if arr[idx] + difference in dic and dic[arr[idx] + difference][bisect.bisect_right(dic[arr[idx] + difference], idx) - (bisect.bisect_right(dic[arr[idx] + difference], idx) == len(dic[arr[idx] + difference]))] > idx:
                cache[idx] = 1 + calc(dic[arr[idx] + difference][bisect.bisect_right(dic[arr[idx] + difference], idx)]) 
                return cache[idx]
            cache[idx] = 1
            return cache[idx]
        
        for i in range(len(arr)):
            dic[arr[i]].append(i)
        print(dic)
        res = 0
        for i in range(len(arr) -1, -1, -1):
            res = max(res, calc(i))
        
        print(cache)
        return res
        