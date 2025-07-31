class Solution:
    def numOfSubsequences(self, s: str) -> int:
        """
        LLCCTCT
        L = [2, 1, 0, 0]
        C = [1, 1, 1, 0]
        T = [1, 1, 1, 1]     

        CX = [0, 0, 2, 2, 0, 1]
        CX_suffix = [0, 0, 5, 3, 1, 1]
        LLMCT
        """
        # Original
        def t_end(string):
            res = 0
            string += "T"
            L, T = 0, string.count("T")
            for i in range(len(string)):
                L += string[i] == "L"
                T -= string[i] == "T"
                if string[i] == "C":
                    res += L * T
            return res
        def l_start(string):
            # LCT
            res = 0
            string = "L" + string
            L, T = 0, string.count("T")
            for i in range(len(string)):
                L += string[i] == "L"
                T -= string[i] == "T"
                if string[i] == "C":
                    res += L * T
            return res
            
        res = max(t_end(s), l_start(s))
        
        curr = 0
        L, T = 0, s.count("T")
        for i in range(len(s)):
            L += s[i] == "L"
            T -= s[i] == "T"
            if s[i] == "C":
                curr += L * T
        print('res', res)
        print('curr', curr)
        L, T = 0, s.count("T")
        a = 0
        for i in range(len(s)):
            L += s[i] == "L"
            T -= s[i] == "T"
            a = max(a, curr + L * T)
        return max(res, a)