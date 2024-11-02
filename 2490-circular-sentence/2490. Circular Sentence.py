class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        a = sentence.split()
        lastWord = a[-1]
        for i in range(1, len(a)):
            if a[i][0] != a[i-1][-1]:
                return False
            lastWord = a[i]
        print(lastWord)
        return sentence[0] == lastWord[-1]
