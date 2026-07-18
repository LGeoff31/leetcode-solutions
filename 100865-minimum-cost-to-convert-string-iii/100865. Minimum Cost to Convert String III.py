class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        @cache
        def dfs(i): # returns the cost of 
            if i == len(source):
                return 0

            res = 1e9

            if source[i] == target[i]:
                res = min(res, dfs(i+1))

            for (pattern, replacement), cost in zip(rules, costs):
                m = len(pattern)
                if i + m > len(source):
                    continue 

                if target[i: i+m] != replacement:
                    continue 

                wild_cards = 0
                valid = True
                for j,c in enumerate(pattern):
                    if c == "*":
                        wild_cards += 1
                    elif c != source[i+j]:
                        valid = False 
                        break 
                if valid:
                    res = min(res, dfs(i+m) + cost + wild_cards)
                    
            return res

        final_result = dfs(0)
        return final_result if final_result != 1e9 else -1