class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        res = []
        
        """
        words = [run, ru, r]
        output = [2, 3, 2]

        1) Find the max prefix among all words (words[i], words[j])
        2) Only if you remove a word at i or j and there isn't backup, will length shrink
        Note that this will only happen in those two instances which is small

        Sliding window??
        """

        def longest_prefix(a,b):
            cnt = 0
            for i in range(min(len(a), len(b))):
                if a[i] == b[i]:
                    cnt += 1
                else:
                    return cnt
            return cnt
            
        def calc_prefix(arr):
            res = [0]
            curr = 0
            for i in range(len(arr) -2, -1, -1):
                curr = max(curr, longest_prefix(arr[i], arr[i+1]))
                res.append(curr)
            return res[::-1]
        if len(words) == 1:
            return [0]
        left_prefix = calc_prefix(words[::-1])[::-1]
        right_prefix = calc_prefix(words)
        # print(left_prefix, right_prefix)
        for i in range(len(words)):
            if i == 0:
                res.append(right_prefix[1])
            elif i == len(words) - 1:
                res.append(left_prefix[len(words) - 2])
            else:
                m = longest_prefix(words[i-1], words[i+1])
                res.append(max(left_prefix[i-1], right_prefix[i+1], m))
        return res