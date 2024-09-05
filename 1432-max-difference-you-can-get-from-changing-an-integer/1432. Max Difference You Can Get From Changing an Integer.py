class Solution:
    def maxDiff(self, num: int) -> int:
        # Find maximum possible num
        a = list(str(num))
        for i in range(len(a)):
            if a[i] != "9":
                store = a[i]
                for j in range(len(a)):
                    if a[j] == store:
                        a[j] = "9"
                break
        a_str = "".join(a)
        print(a_str)
        # Find minimum possible num
        b = list(str(num))
        for i in range(len(b)):
            if i == 0:
                if b[i] != "1":
                    store = b[i]
                    for j in range(len(b)):
                        if store == b[j]:
                            b[j] = "1"
                    break
            elif b[i] != "1" and b[i] != "0": 
                store = b[i]
                for j in range(len(b)):
                    if store == b[j] and store != "0":
                        b[j] = "0"
                break
        b_str = "".join(b)
        print(b_str)
        return int(a_str) - int(b_str)

        