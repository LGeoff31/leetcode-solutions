class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        lst = [words[0]]
        amountSpaces = 0
        stringLength = len(words[0])
        for word in words[1:]:
            if stringLength + 1 + len(word) + amountSpaces <= maxWidth: #can add new word
                lst.append(word)
                print(lst)
                stringLength += len(word)
                amountSpaces+=1
            else: #if next word no longer fits
                print(amountSpaces)
                spacesPerGap = 0
                if amountSpaces!= 0: 
                    spacesPerGap = (maxWidth-stringLength) // amountSpaces
                    remainder = (maxWidth-stringLength) % amountSpaces
                    print(spacesPerGap)
                    print(remainder)
                a = ""
                if len(lst) == 1:
                    a += lst[0] + " " * (maxWidth - stringLength)
                else:
                    for i in range(len(lst)):
                        if i == len(lst)-1:
                            a += lst[i]
                        else:
                            if remainder != 0:
                                a += lst[i] + (" " * (spacesPerGap+1))
                                remainder -= 1
                            else:
                                a += lst[i] + (" " * (spacesPerGap))

                res.append(a)
                lst = [word]
                stringLength = len(word)
                amountSpaces=0
            # print(lst)
        a = ""
        for i,word in enumerate(lst):
            if i == len(lst)-1: a += word
            else: a += word + " "

        res.append(a)
            
        remain = maxWidth - len(a)
        res[-1] += " "*remain
        return res
        