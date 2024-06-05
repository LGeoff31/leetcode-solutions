class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alphabet = set()
        for i in range(26):
            alphabet.add(chr(i + 97))
        
        res = []
        for letter in alphabet:
            min_count = 1e9
            for word in words:
                dic = Counter(word)
                if letter not in dic:
                    min_count = 0
                else:
                    min_count = min(min_count, dic[letter])
            for i in range(min_count):
                res.append(letter)

        return res


        