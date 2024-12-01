class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def convert(string):
            res = 0
            res += 60 * int(string[2:])
            res += int(string[:2]) * 3600
            return res
        dic = defaultdict(list)
        for name, time in access_times:
            dic[name].append(convert(time))
        res = []
        for name in dic:
            arr = dic[name]
            arr.sort()
            for i in range(len(arr) - 2):
                if arr[i+2] - arr[i] < 3600:
                    res.append(name)
                    break
        return res

        print(dic)
        return []