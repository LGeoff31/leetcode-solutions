class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:   
        vowels = set()
        vowels.add("a")
        vowels.add("e")
        vowels.add("i")
        vowels.add("o")
        vowels.add("u")
        res = 0
        lst = []
        if s[0] in vowels: lst.append(1)
        else: lst.append(0)
        for i in range(1, len(s)):
            if s[i] in vowels:
                lst.append(lst[-1] +1)
            else:
                lst.append(lst[-1])
        res = 0
        print(lst)
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if i == 0: v = lst[j]
                else: v = lst[j]-lst[i-1]
                elements = j-i+1
                c = elements-v
                if c==v and c*v%k==0:
                    print(i, j)
                    res += 1
        return res

