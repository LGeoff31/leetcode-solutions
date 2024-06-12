class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def equal(str1, str2):
            a,b, c, d = {}, {}, {}, {}
            for i in range(len(str1)):
                if i%2 == 0:
                    a[str1[i]] = 1 + a.get(str1[i], 0)
                    c[str2[i]] = 1 + c.get(str2[i], 0)
                else:
                    b[str1[i]] = 1 + b.get(str1[i], 0)
                    d[str2[i]] = 1 + d.get(str2[i], 0)
            return a == c and b == d
        
        res = 1
        curr = 0
        visited = set()
        for i in range(len(words)):
            if i in visited:
                continue
            visited.add(i)
            for j in range(len(words)):
                if equal(words[i], words[j]) and j not in visited:
                    visited.add(j)
            print(visited)
            if len(visited) == len(words):
                break
            res += 1

        return res

