class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split(".")
        b = version2.split(".")
        diff = abs(len(a) - len(b))
        for i in range(diff):
            if len(a) > len(b):
                b.append("0")
            else:
                a.append("0")

        
        def remove_leading_zeros(string):
            for i in range(len(string)):
                if string[i] != "0":
                    return string[i:]
            return "0"
        
        for i in range(len(a)):
            a[i] = remove_leading_zeros(a[i])
        
        for i in range(len(b)):
            b[i] = remove_leading_zeros(b[i])
        

        print(a)
        print(b)
        for i in range(len(a)):
            if int(a[i]) > int(b[i]):
                return 1
            elif int(a[i]) < int(b[i]):
                return -1
        return 0