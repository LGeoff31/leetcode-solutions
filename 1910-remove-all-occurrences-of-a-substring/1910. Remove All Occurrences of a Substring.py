class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            for i in range(len(s) - len(part)+1): #12-3 = 9
                possible = s[i:i+len(part)]
                print("possible", possible)
                if possible == part:
                    s = s[0:i] + s[i+len(part):]
                    print(s)
                    break
                # print(s)
        return s

        