class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum_word_length = min(len(word) for word in strs)
        base_word = strs[0]
        longest_common_prefix = ""

        for j in range(minimum_word_length):
            for i in range(len(strs)):
                current_word = strs[i]
                if current_word[j] != base_word[j]:
                    return longest_common_prefix 
            longest_common_prefix += base_word[j]
        return longest_common_prefix