class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i in range(len(colors)):
            dic[colors[i]].append(i)
        res=[]
        print(dic)
        for idx, c in queries:
            if not dic[c]: 
                res.append(-1)
                continue

            i = bisect_left(dic[c], idx)
            a = 1e9
            if i >= len(dic[c]):
                a = min(a, abs(idx-dic[c][i-1]))
            else:
                a = abs(dic[c][i]-idx)
                if i+1 < len(dic[c]):
                    a = min(a, abs(dic[c][i+1] - idx))
                if i-1 >= 0:
                    a = min(a, abs(dic[c][i-1] - idx))

            # left_side_idx = dic[c][bisect_left(dic[c], idx)]
            # right_side_idx = dic[c][bisect_left(dic[c], idx)]
            res.append(a)

        return res