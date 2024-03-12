class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        wordcount={}
        for word in words:
            wordcount[word]=1+wordcount.get(word,0)
        result=[]
        substringlength=len(words)*len(words[0])
        for i in range(len(s)-substringlength+1):
            substr=s[i:i+substringlength]
            substrcount={}
            for j in range(0,len(substr),len(words[0])):
                word=substr[j:j+len(words[0])]
                substrcount[word]=1+substrcount.get(word,0)
            if substrcount==wordcount:
                result.append(i)
        return result