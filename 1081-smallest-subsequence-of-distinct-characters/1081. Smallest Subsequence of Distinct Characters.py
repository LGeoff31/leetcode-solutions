class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        bcabc

        [a,b,c]


        cbacdcbc
        [a,c,d,]

        cbaacabcaaccaacababa
        [a,b]
        """
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        

        stack = []
        used = set()

        for i in range(len(s)):
            if s[i] in used:
                continue
            while stack and s[i] < stack[-1] and last[stack[-1]] > i:
                used.remove(stack.pop())
            print(stack)
            if s[i] not in used:
                used.add(s[i])
                stack.append(s[i])
        return "".join(stack)

