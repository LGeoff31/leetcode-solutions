class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # If it ever becomes Bob' turn with a even # of vowels, he will always win, hence for Alice to win she must always leave an odd # of vowels for Bob's turn
        vowels = sum(1 for c in  s if c in {"a", "e", "i", "o", "u"})
        if vowels == 0:
            return False
        return True