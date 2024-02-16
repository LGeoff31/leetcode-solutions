class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        if len(str2) < len(str1):
            for i in range(len(str2)):
                for j in range(i, len(str2)):
                    substring = str2[i:j+1]
                    if len(str1) % len(substring) == 0  and len(str2) % len(substring) == 0:
                        amountTimes = len(str1) //  len(substring)
                        amountTimes2 = len(str2) //  len(substring)

                        if substring * amountTimes == str1 and substring * amountTimes2 == str2 and len(substring) > len(res):
                            res = substring 
        else:
             for i in range(len(str1)):
                for j in range(i, len(str1)):
                    substring = str1[i:j+1]
                    if len(str2) % len(substring) == 0 and len(str1) % len(substring) == 0:
                        amountTimes = len(str2) //  len(substring)
                        amountTimes2 = len(str1) //  len(substring)

                        if substring * amountTimes == str2 and substring * amountTimes2 == str1 and len(substring) > len(res):
                            res = substring 
        return res

        TAUXXTAUXXTAUXX
        TAUXXTAUXXTAUXXTAUXXTAUXX
        TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX
