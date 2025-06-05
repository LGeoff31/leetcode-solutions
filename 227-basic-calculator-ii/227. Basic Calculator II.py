class Solution:
    def calculate(self, s: str) -> int: #2-3/2 -> 1
        """
        Have a stack or both the numbers and operations
        Whenever the operations is a / or *, apply that algorithm on the last two digits since its forced
        At the end clean up via the + or - respectively
        """
        s = s.replace(" ", "")
        print('s', s)
        s += "/"
        operations = []
        numbers = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            num = 0
            # Extract the number    
            while i < len(s) and s[i] not in "+/-*" and s[i] != " ":
                num = 10 * num + int(s[i])
                i += 1
            numbers.append(num)
            if operations and operations[-1] in "/*":
                a = numbers.pop()
                b = numbers.pop()
                if operations[-1] == "/":
                    numbers.append(b//a)
                    operations.pop()
                else:
                    numbers.append(b*a)
                    operations.pop()
            if s[i] != " ":
                operations.append(s[i])
            i += 1
            # print(numbers)
            # print(operations)
        operations=operations[:-1]
        # print()
        # print(numbers)
        # print(operations)
        idx = 0
        res = numbers[0] 
        while idx < len(operations):
            if operations[idx] == "+":
                res += numbers[idx + 1]
            else:
                res += -numbers[idx + 1]
            idx += 1
           
        
        return res