class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        dic = defaultdict(list)
        for word in allowed:
            dic[word[:2]].append(word[2])
        def dfs(string):
            if len(string) == 1:
                return True
            next_level = []
            for i in range(len(string) - 1):
                pair = string[i:i+2]
                if pair in dic:
                    next_level.append(dic[pair])
                else:
                    return False 
            for combination in product(*next_level):
                if dfs("".join(combination)):
                    return True
            return False
        return dfs(bottom)
          