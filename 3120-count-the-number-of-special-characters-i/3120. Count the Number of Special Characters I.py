class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        a = Counter(word)
        visited=set()
        for key in a:
            if key == key.lower() and key not in visited:
                visited.add(key)
                if key.upper() in a:
                    res+=1

        return res