class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary, key=len)
        lst = sentence.split()
        res = []
        for word in lst:
            found = False
            for w in dictionary:
                if len(w) <= len(word) and w == word[:len(w)]:
                    res.append(w)
                    found = True
                    break
            if not found:
                res.append(word)
        return " ".join(res)

