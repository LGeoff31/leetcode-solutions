class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_frequencies = {}
        global_max = 0
        l = 0
        r = 0
        # s = "abcabcbb"
        #              ^
        # {a : 1, b: 2, c: 1}
        while r < len(s):
            local_max = 0
            duplicate_char = s[r]
            # Continue expanding our window until we reach a duplicate
            while r < len(s):
                if s[r] in letter_frequencies:
                    duplicate_char = s[r]
                    letter_frequencies[s[r]] += 1
                    break
                
                letter_frequencies[s[r]] = 1
                r += 1

            local_max = r-l
            global_max = max(local_max, global_max)

            # Slide left pointer to make it a valid window
            while letter_frequencies[duplicate_char] > 1:
                letter_frequencies[s[l]] -= 1
                if letter_frequencies[s[l]] == 0:
                    del letter_frequencies[s[l]]
                l += 1
            r += 1

        return global_max