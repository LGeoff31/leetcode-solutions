class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # bank, kanb
        # leftWrongChars = [b, k]
        # rightWrongChars = [k, b]
        leftWrongChars = []
        rightWrongChars = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                leftWrongChars.append(s1[i])
                rightWrongChars.append(s2[i])
                if len(leftWrongChars) > 2:
                    return False
        return leftWrongChars == rightWrongChars[::-1]