class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = sorted(meetings, key=lambda x: x[-1])
        self.visited = set() #people who know the secret
        self.visited.add(0)
        self.visited.add(firstPerson)
        i = 0

        def dfs(dic, key):
            for neighbor in dic[key]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    dfs(dic, neighbor)
            
        res = []
        while i < len(meetings):
            lst = [meetings[i]]
            j = i+1
            while j < len(meetings) and meetings[j][-1] == lst[-1][-1]:
                lst.append(meetings[j])
                i = j
                j+=1
            i += 1
            res.append(lst)
        print(res)
        for arr in res:
            dic = {}
            for entry in arr:
                if entry[0] in dic: dic[entry[0]].append(entry[1])
                else: dic[entry[0]] = [entry[1]]
                if entry[1] in dic: dic[entry[1]].append(entry[0])
                else: dic[entry[1]] = [entry[0]]
            for key in dic:
                if key in self.visited:
                    dfs(dic, key)

        # print(self.visited)
        return list(self.visited)
