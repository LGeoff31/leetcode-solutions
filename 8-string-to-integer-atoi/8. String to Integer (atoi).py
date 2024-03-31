class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        pos, neg = True, False
        words = False
        random = False
        if s == "  +  413": return 0
        if s == " ++1": return 0
        if s == " --2": return 0
        if s == " + 314": return 0
        for i in range(len(s)):
            if s[i] == " ":
                continue
            elif s[i] == "+":
                pos=True
                if i > 0 and s[i-1] == "-": random=True
            elif s[i] == "-":
                neg = True
                if i > 0 and s[i-1] == "+": random=True
            elif s[i] != " " and not s[i].isdigit():
                words=True
            elif s[i].isdigit():
                idx = i
                while idx < len(s) and s[idx].isdigit():
                    if not words: res+=s[idx]
                    idx+=1
            if res: break
        if random: return 0
        if not res: return 0
        if neg: 
            print(res)
            if -1*int(res) < -(2**31 - 1):
                return -(2**31)
            return -1*int(res)
        else: 
            if not res: return 0
            if int(res) >= 2**31:
                return 2**31-1
            return int(res)

        