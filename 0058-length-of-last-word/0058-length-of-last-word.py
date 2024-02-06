class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            if s[0] != " ":
                return 1
            return 0
        length = 0
        found = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and found == True and i != len(s)-1:
                return length
            if s[i] != " ":
                found = True
            
                length += 1
                print('reached')
                if i == 0:
                    return length
        return -1
        