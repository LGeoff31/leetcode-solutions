class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        a = 0
        c = set(bannedWords)
        for b in message:
            if b in c:
                a += 1
        return a >= 2
        