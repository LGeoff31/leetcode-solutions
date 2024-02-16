class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ""
        #case where a or b == 1
        while a > 0 and b > 0:
            if a == b:
                s += "a"
                a-=1
                if a == 0: 
                    break
                s += "b"
                b -= 1
                if b == 0: 
                    break

                s += "a"
                a -= 1
                if a == 0: 
                    break
            elif a > b:
                s += "a"
                a-=1
                if a == 0: 
                    break
                s += "a"
                a -= 1
                if a == 0: 
                    break

                s += "b"
                b -= 1
                if b == 0: 
                    break
            else:
                s += "b"
                b-=1
                if b == 0: 
                    break
                s += "b"
                b -= 1
                if b == 0: 
                    break

                s += "a"
                a -= 1
                if a == 0: 
                    break
        if a != 0:
            for i in range(a):
                s += "a"
        else:
            for i in range(b):
                s += "b"
        return s