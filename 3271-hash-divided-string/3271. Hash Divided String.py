class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        lst=[]
        for i in range(0, len(s) - k + 1, k):
            lst.append(s[i:i+k])
        res = ""
        print(lst, ord("a"))
        for item in lst:
            print((sum(ord(char)-96 for char in item)))
            res += chr((sum(ord(char)-97 for char in item)) % 26 + 97)
        return res
        

        

        