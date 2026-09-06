class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        for i, word in enumerate(sentence.split()):
            print(re.match(r'["aeiouAEIOU"]', word))
            if re.match(r'["aeiouAEIOU"]', word):
                res.append(word + "ma" + "a" * (i+1))
            else:
                res.append(word[1:] + word[0] + "ma" + "a" * (i+1))
            
        return " ".join(res)