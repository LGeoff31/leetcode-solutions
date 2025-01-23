class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        n = len(words)
        prefix = [0] * n

        def abbr(word, idx): # abba -> 2
            if (len(word) - idx) <= 3: return word

            return word[:idx+1] + str(len(word) - idx - 2) + word[-1]
        lst = [abbr(word, 0) for word in words]

        for i in range(n):
            while True:
                duplicates = set()
                for j in range(i+1, n):
                    if i != j and lst[i] == lst[j]:
                        duplicates.add(j)
                if not duplicates: break
                duplicates.add(i)
                for k in duplicates:
                    prefix[k] += 1
                    lst[k] = abbr(words[k], prefix[k])
                # lst = [abbr(words[i], prefix[i]) for i in range(len(words))]

        return lst