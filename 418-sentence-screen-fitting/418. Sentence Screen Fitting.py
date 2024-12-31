class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        idx, res = 0, 0
        memo = {} # word_idx : [complete_word_count, next_start_word_idx]

        for _ in range(rows):
            start_word_idx = idx
            if start_word_idx in memo:
                _count, _idx = memo[start_word_idx]
                idx = _idx
                res += _count
            else:
                complete_word_count = 0

                col = 0
                if len(sentence[idx]) > cols:
                    return 0
                while col + len(sentence[idx]) <= cols:
                    col += len(sentence[idx])
                    if col < cols:
                        col += 1

                    idx = (idx + 1) % len(sentence)
                    if idx == 0: 
                        complete_word_count += 1
                memo[start_word_idx] = [complete_word_count, idx]
                res += complete_word_count

        return res