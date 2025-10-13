class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def anagram(w1, w2):
            a,b = Counter(w1), Counter(w2)
            if len(a) != len(b): return False
            for key in a:
                if key not in b or a[key] != b[key]:
                    return False
            return True
        
        while True:
            found = False
            if not words: break
            new_lst = [words[0]]
            for i in range(1, len(words)):
                if anagram(words[i], words[i-1]):
                    continue
                else:
                    new_lst.append(words[i])
            words = new_lst
            if not found:
                break
        return words
