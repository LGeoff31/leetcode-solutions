class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        prefix = [0] +list(accumulate(capacity))

        indicies = defaultdict(list)
        for i, val in enumerate(capacity):
            indicies[val].append(i)

        def calc(val): 
            cnt = 0
            dic = defaultdict(int)
            target_val = 3 * val
            lst = indicies[val]
            p = 0

            for i in range(len(lst)):
                r = lst[i]
                while p < i and lst[p] <= r-2:
                    dic[prefix[lst[p] + 1]] += 1
                    p += 1
                cnt += dic[prefix[r] - val]
            return cnt
        res = 0
        for val in indicies:
            res += calc(val)

        return res
            