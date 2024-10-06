class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Idea, you can insert on left-most side, right-most side, or in the middle

        prefix = suffix = 0
        a,b = sentence1.split(), sentence2.split()
        if len(a) == len(b) and a != b: return False
        if len(a) < len(b):
            return self.areSentencesSimilar(sentence2, sentence1)
        
        # Sentence 1 will always be larger
        for i in range(len(b)):
            if b[i] == a[i]:
                prefix += 1
            else:
                break
        for i in range(len(b) - 1, -1, -1):
            if b[i] == a[len(a) - 1 - (len(b) - i - 1)]:
                suffix += 1
            else:
                break
        print(prefix, suffix)
        if prefix == len(b) or suffix == len(b) or prefix + suffix >= len(b):
            return True 
        return False