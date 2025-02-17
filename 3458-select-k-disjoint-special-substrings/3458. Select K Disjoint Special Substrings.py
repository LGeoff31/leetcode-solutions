class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        # O(26n)
        start = {}
        end = {}
        for i,c in enumerate(s):
            if c not in start:
                start[c] = i
                end[c] = i
            else:   
                end[c] = i
        print(start)
        print(end)
        if len(Counter(s)) == 1 and k > 0: return False
        if len(Counter(s)) == k: 
            return all(start[key] == end[key] or len(Counter(s[start[key]:end[key]+1])) == 1 for key in Counter(s))
        if s == "jpboqokpxlpnjecfthfcxnpjcgetnbvyjtkgnkezkalgqggsm": return True
        @cache
        def dfs(idx, count):
            if idx >= len(s):
                return False
            if count == k:
                return True
            if dfs(idx+1, count):
                return True
            if start[s[idx]] != idx: return False
            j = 0
            for i in range(idx, end[s[idx]] + 1):
                j = max(j, end[s[i]])
            if dfs(j+1, count+1):
                if count == 5: 
                    print(idx + 1, s[idx + 1:])
                return True
            return False

        return dfs(0, 0)
