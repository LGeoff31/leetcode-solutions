class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_dic = defaultdict(list)
        for allow in allowed:
            allowed_dic[allow[:2]].append(allow[2])

        def dfs(layer):
            # print('calling', layer)
            if len(layer) == 1:
                return True
            
            # For the current layer, try every possibility
            tmp = []
            for i in range(len(layer) - 1):
                key = layer[i: i+2]
                if key not in allowed_dic: return False
                options = allowed_dic[key]
                tmp.append(options)
            lst = [''.join(p) for p in product(*tmp)]
            # print('lst', lst)
            for lst_option in lst:
                if dfs(lst_option):
                    return True 
            return False

        return dfs(bottom)