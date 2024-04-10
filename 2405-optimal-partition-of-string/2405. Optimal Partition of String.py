class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[s[i]].append(i)
        last = 1e9
        print(dic)
        for i in range(len(s)):
            if i == last: 
                count+=1
                last = 1e9
            if bisect.bisect_right(dic[s[i]], i) == len(dic[s[i]]):
                print(i, last, 'gay')
            else:
                last = min(last, dic[s[i]][bisect.bisect_right(dic[s[i]], i)])
            print(i, last)
        return count+1

        