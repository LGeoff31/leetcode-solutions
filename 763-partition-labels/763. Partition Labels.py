class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(list)

        for i in range(len(s)):
            dic[s[i]].append(i)

        lst = []
        for key in dic:
            lst.append((dic[key][0], dic[key][-1], key))
        lst.sort()

        grouping = []

        prevEnding = lst[0][0] + 1

        group = []
        for i in range(len(lst)):
            start, end, letter = lst[i]
            if start < prevEnding: #overlap
                group.append(letter)
            else:
                grouping.append(group)
                group = []
                group.append(letter)
            prevEnding = max(prevEnding, end)
        grouping.append(group)
        res = []

        for group in grouping:
            minimum, maximum = 1e9, 0
            for key in dic:
                if key in group:
                    minimum = min(minimum, dic[key][0])
                    maximum = max(maximum, dic[key][-1])
            res.append(maximum - minimum + 1)
        return res
       
        