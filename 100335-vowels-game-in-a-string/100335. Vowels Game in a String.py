class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # If it ever becomes Bob' turn with a even # of vowels, he will always win, hence for Alice to win she must always leave an odd # of vowels for Bob's turn
        vowels = 0
        for i in range(len(s)):
            if s[i] in ["a", "e", "i", "o", "u"]:
                vowels += 1
        if vowels == 0:
            return False
        if vowels % 2 == 1:
            return True
        return vowels % 2 == 0
        