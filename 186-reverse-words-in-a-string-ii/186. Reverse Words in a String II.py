class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lst = []
        idx = 0
        while idx < len(s):
            word = ""
            while idx < len(s) and s[idx] != " ":
                word += s[idx]
                idx += 1
            lst.append(word)
            idx += 1
        lst = lst[::-1]
        idx = 0
        for word in lst:
            for c in word:
                s[idx] = c
                idx += 1
            if idx >= len(s): break
            s[idx] = " "
            idx += 1
        
        print(lst)
        
        # l, r = 0, len(s) - 1
        # while l <= r:
        #     length_first_word = 0
        #     length_second_word = 0
        #     temp_l = l
        #     temp_r = r
        #     while s[temp_l] != " ":
        #         length_first_word += 1
        #         temp_l += 1
        #     while s[temp_r] != " ":
        #         length_second_word += 1
        #         temp_r -= 1
            
            