class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        print(ord('a'), ord("A"), ord('a') - ord('A'))

        for i in range(len(s)):
            print(stack)
            valid = True
            if s[i].isupper():
                if stack and stack[-1].upper() == s[i] and stack[-1] != s[i]:
                    stack.pop()
                    valid = False
            else:
                if stack and stack[-1].lower() == s[i] and stack[-1] != s[i]:
                    stack.pop()
                    valid = False

            if valid: stack.append(s[i])
        return "".join(stack)

      