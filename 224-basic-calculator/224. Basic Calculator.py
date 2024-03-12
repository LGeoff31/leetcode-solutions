class Solution:
    def calculate(self, s: str) -> int:
        #remove all spaces
        #evaluate all brackets immediately
        num = 0
        sign = 1
        res = 0
        stack = []
        for i in range(len(s)): # iterate till last character
            c = s[i]
            if c.isdigit(): # process if there is digit
                num = num*10 + int(c) # for consecutive digits 98 => 9x10 + 8 = 98
            elif c in '-+': # check for - and +
                res += num*sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res +=sign*num
                res *=stack.pop()
                res +=stack.pop()
                num = 0
        return res + num*sign
        