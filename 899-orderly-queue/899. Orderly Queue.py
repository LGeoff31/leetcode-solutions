class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # Given any string s, we can get the kth smallest letters to appear in lexigoraph order 
        # Now the question is trying to make s[k+1:] lexigoraphicall smallest
        # O(nk)
        if k == 1:
            lst = []
            indexes = []
            smallest = min(s)
            for i in range(len(s)):
                if s[i] == smallest:
                    lst.append(s[i:] + s[:i])
            return sorted(lst)[0]
            # idx = s.index(min(s))
            # return min(s) + s[idx+1 : ] + s[:idx]
        return "".join(sorted(s))
        # lst = SortedList()
        # for c in s:
        #     lst.add(c)
        

        # prefix_goal = "".join(lst[:k])
        # print('p', prefix_goal)
        # # O (NK)
        # while s[:k] != prefix_goal:
        #     max_char = max(s[:k])
        #     idx_max_char = s.index(max_char)
        #     s = s[:idx_max_char] + s[idx_max_char + 1 : ] + max_char
        #     print(s)
        # return s