class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        def valid(word):
            i, j = 0, 0
            while i < len(word) and j < len(pattern):
                if word[i] != pattern[j]:
                    if word[i] == word[i].upper():
                        return False
                    i += 1
                else:
                    i += 1
                    j += 1
            if i == len(word) and j == len(pattern):
                return True
        
            if j != len(pattern):
                return False
            while i < len(word):
                if word[i] == word[i].upper():
                    return False
                i += 1
            return True
        for word in queries:

            res.append(valid(word))
        return res