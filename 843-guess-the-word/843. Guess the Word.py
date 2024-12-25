# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def eliminateWords(guess, matches):
            lst = []
            for word in words:
                similarity = 0
                for i in range(len(word)):
                    similarity += word[i] == guess[i]
                if similarity == matches:
                    lst.append(word)
            return lst

        def generateBestWord():
            count = [[0] * 26 for _ in range(6)]
            for idx, word in enumerate(words):
                for i in range(len(word)):
                    count[i][ord(word[i]) - 97] += 1
            bestWordScore = 0
            bestWord = ""
            for idx, word in enumerate(words):
                score = 0
                for i in range(len(word)):
                    score += count[i][ord(word[i]) - 97]
                if score > bestWordScore:
                    bestWordScore = score
                    bestWord = word
            return bestWord

        while words:
            guess = generateBestWord()
            matches = master.guess(guess) 
            if matches == 6:
                return
            words = eliminateWords(guess, matches)

