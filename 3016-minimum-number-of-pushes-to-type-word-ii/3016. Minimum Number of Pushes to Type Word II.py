from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = Counter(word)
        dic = dict(sorted(dic.items(), key = lambda x: x[1], reverse=True))
        print(dic)
        total = 0
        if len(dic) <= 8:
            for key in dic:
                total += dic[key]
            return total
        elif len(dic) <= 16: #15
            count = 1
            z = 1
            for key in dic:
                total += dic[key] * z
                count += 1
                if count == 9:
                    z += 1
        elif len(dic) <= 24:
            count = 1
            z = 1
            for key in dic:
                total += dic[key] * z
                count += 1
                if count == 9:
                    z += 1
                if count == 17:
                    z += 1
        else:
            count = 1
            z = 1
            for key in dic:
                total += dic[key] * z
                count += 1
                if count == 9:
                    z += 1
                if count == 17:
                    z += 1
                if count == 25:
                    z += 1
            
        return total