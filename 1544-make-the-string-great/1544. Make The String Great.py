class Solution:
    def makeGood(self, s: str) -> str:
        print(ord("a"), ord("A"), ord("B"))
        a,b = 97, 65
        lst = []
        for i in range(26):
            lst.append([a,b])
            lst.append([b,a])
            a+=1
            b+=1
        dic = {chr(lower):chr(upper) for lower, upper in lst}
        stack = [s[0]]

        for i in range(1, len(s)):
            if stack and dic[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
        