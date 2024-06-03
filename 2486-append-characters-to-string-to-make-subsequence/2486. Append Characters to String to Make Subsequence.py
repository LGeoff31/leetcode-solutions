class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res = 0
        ptr1, ptr2 = 0, 0
        for i in range(len(s)):
            if s[ptr1] == t[ptr2]:
                ptr2 += 1
            ptr1+=1
            if ptr2 >= len(t): break
        return len(t) - ptr2 
        