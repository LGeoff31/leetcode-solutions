class Trie:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        self.curr = self.root
        self.curr_sentence = []
        for sentence, time in zip(sentences, times):
            self.add_to_trie(sentence, time)
        self.dead = Trie()

    def add_to_trie(self, sentence, count):
        curr = self.root
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
            curr.sentences[sentence] += count


    def input(self, c: str) -> List[str]:
        if c == "#":
            self.curr_sentence = "".join(self.curr_sentence)
            self.add_to_trie(self.curr_sentence, 1)
            self.curr_sentence = []
            self.curr = self.root
            return []
        self.curr_sentence.append(c)
        if c not in self.curr.children:
            self.curr = self.dead
            return []
        self.curr = self.curr.children[c]
        sentences = self.curr.sentences

        sorted_sentences = sorted(sentences.items(), key = lambda x: (-x[1], x[0]))
        ans = []
        for i in range(min(3, len(sorted_sentences))):
            ans.append(sorted_sentences[i][0])
        return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)