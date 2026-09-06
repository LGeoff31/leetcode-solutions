class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)
        paragraph.replace("!?',;.", "")
        word_counter = defaultdict(int)
        for word in re.split(r"[\s!?',;.]+", paragraph):
            if word:
                word_counter[word.lower()] += 1
        print(word_counter)
        max_freq_not_banned = 0
        res = ""
        for word in word_counter:
            if word not in banned_words and word_counter[word] > max_freq_not_banned:
                max_freq_not_banned = word_counter[word]
                res = word
        return res
