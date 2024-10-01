class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        res = 0
        dic = {"a": 1, "b":1, "c": 2, "d": 2, "e": 2, "f": 3, "g": 3, "h": 3, "i": 4, "j":4,"k":4, "l":5, "m":5,"n":5,"o":6,"p":6,"q":6,"r":7,"s":7,"t":7,"u":8,"v":8,"w":8,"x":9,"y":9,"z":9}
        def valid(string):
            count = 0
            for i in string:
                count += dic[i]
            return count % len(string) == 0
            
        prefix = [0] * len(word)
        acc = 0
        for idx, i in enumerate(word):
            acc += dic[i]
            prefix[idx] = acc


        for i in range(len(word)):
            for j in range(i, len(word)):
                if i == 0:
                    if (prefix[j]) % (j-i+1) == 0:
                        res += 1
                else:
                    if (prefix[j] - prefix[i-1]) % (j-i+1) == 0:
                        res += 1

        return res