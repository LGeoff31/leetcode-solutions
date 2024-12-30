from sortedcontainers import SortedList
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        res = 0
        lst = SortedList()
        properties.sort(reverse=True)
        i = 0
        print(properties)
        while i < len(properties):
            a = []
            valid = False
            while i+1 < len(properties) and properties[i][0] == properties[i+1][0]:
                if len(lst) - bisect_right(lst, properties[i][1]) > 0:
                    res += 1
                # res += len(lst) - bisect_right(lst, properties[i][1])
                a.append(properties[i][1])
                i += 1
            a.append(properties[i][1])
            if len(lst) - bisect_right(lst, properties[i][1]) > 0: 
                res += 1
            # res += valid
            i += 1
            for num in a:
                lst.add(num)
            # print(lst, res)

        return res
            