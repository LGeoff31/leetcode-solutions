class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list) # Content: File
        for path in paths:
            lst = path.split()
            source = lst[0]
            for i in range(1, len(lst)):
                open_brace_idx = lst[i].index("(")
                content = lst[i][open_brace_idx+1:-1]
                dic[content].append(source + "/" + lst[i][:open_brace_idx])
        res = []
        for key in dic:
            if len(dic[key]) > 1:
                res.append(dic[key])
        print(dic)
        return res