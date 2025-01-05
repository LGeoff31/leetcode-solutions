from sortedcontainers import SortedList
class Solution:
    def calculateScore(self, s: str) -> int:
        # Find closest unmarked on the leftside of i, s[j] mirrors s[i]
        # Mark i, j, add score by i - j
        score = 0
        dic = defaultdict(SortedList) # chracter to index
        alphabet = [chr(i) for i in range(97, 97 + 26)]
        reverse = alphabet[::-1]
        def mirror(letter):
            return reverse[alphabet.index(letter)]
        marked = set() # Indices of marked 
        for i in range(len(s)): #O(n)
            found = False
            if mirror(s[i]) in dic:
                indicies = dic[mirror(s[i])]
                for idx in range(len(indicies) - 1, -1, -1):
                    if indicies[idx] not in marked:
                        marked.add(indicies[idx])
                        marked.add(i)
                        score += i - indicies[idx]
                        char = mirror(s[i])
                        dic[char].remove(indicies[idx])
                        found = True
                        break
            if not found:
                dic[s[i]].add(i)
                
        return score
            
        