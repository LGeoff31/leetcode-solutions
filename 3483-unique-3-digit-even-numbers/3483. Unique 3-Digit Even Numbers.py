class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        a = set()

        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                for k in range(j+1, len(digits)):
                    x,y,z = digits[i], digits[j], digits[k]
                    if x != 0 and x!=0 and z%2 == 0:a.add(str(x) + str(y) + str(z))
                    if x != 0 and x!=0 and y%2 == 0:a.add(str(x) + str(z) + str(y))
                    if y != 0 and z %2==0: a.add(str(y) + str(x) + str(z))
                    if y != 0 and x%2==0: a.add(str(y) + str(z) + str(x))
                    if z != 0 and y%2==0: a.add(str(z) + str(x) + str(y))
                    if z != 0 and x%2==0: a.add(str(z) + str(y) + str(x))
        print(a)
        return len(a)