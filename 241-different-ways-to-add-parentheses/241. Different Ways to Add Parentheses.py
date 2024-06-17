class Solution:
    def isOperator(self, ch):
        return ch == '+' or ch == '-' or ch == '*'

    def getDiffWays(self, i, j, expression):
        res = []

        # If length of the substring is 1 or 2
        # we encounter our base case i.e. a number found.
        if j - i + 1 <= 2:
            res.append(int(expression[i:j + 1]))
            return res

        # If it is not a number then it is an expression
        # now we try to evaluate every opertor present in it
        for ind in range(i, j + 1):
            if self.isOperator(expression[ind]):
                op = expression[ind]
                
                # if char at ind is operator 
                # get all results for its left and right substring using recursion
                left = self.getDiffWays(i, ind - 1, expression)
                right = self.getDiffWays(ind + 1, j, expression)

                # try all options for left & right operand
                # and push all results to the answer
                for l in left:
                    for r in right:
                        if op == '+':
                            res.append(l + r)
                        elif op == '-':
                            res.append(l - r)
                        elif op == '*':
                            res.append(l * r)

        return res

    def diffWaysToCompute(self, expression: str):
        n = len(expression)
        return self.getDiffWays(0, n - 1, expression)