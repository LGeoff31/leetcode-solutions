class Solution:
    def decodeString(self, s: str) -> str:
        while s.count("[") != 0:
            res = ""
            a = 0
            while a < len(s):
                newString = ""
                if s[a].isdigit():
                    number = ""
                    for i in range(a, len(s)):
                        if s[i].isdigit():
                            number += s[i]
                            a = i+2
                        else:
                            break

                    number = int(number)
                    openBracketCount = 1
                    closeBracketCount = 0
                    for j in range(a, len(s)):
                        if s[j] == "]" and openBracketCount - 1 == closeBracketCount:
                            a = j+1
                            break
                        elif s[j] == "]":
                            closeBracketCount += 1
                            newString += s[j]
                        elif s[j] == "[":
                            openBracketCount += 1
                            newString += s[j]
                        else:
                            newString += s[j]
                    res += newString * number
                else:
                    res += s[a]
                    a += 1
            s = res
        return s 
                



        