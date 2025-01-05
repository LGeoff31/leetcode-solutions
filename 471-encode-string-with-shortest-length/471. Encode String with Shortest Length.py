class Solution: 
    @lru_cache(None)
    def encode(self, s: str) -> str:
        i = (s+s).find(s,1)
        res = str(len(s) // i) + "[" + self.encode(s[:i]) + "]" if i < len(s) else s
        ans = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, len(s))]
        return min(ans + [res],key = len)
        #"abcabcabcabc"
        # self.ans = s
        # def find_new_idx(idx, pattern):
        #     while idx + len(pattern) <= len(s):
        #         if s[idx : idx + len(pattern)] == pattern:
        #             idx += len(pattern) # 9
        #         else:
        #             break
        #     return idx # Returns 9
        # def dfs(idx, res):
        #     print('abaha')
        #     if idx == len(s):
        #         print('reached', res)
        #         if len(res) < len(self.ans):
        #             self.ans = res
        #         return
        #     for i in range(idx+1, len(s) + 1):
        #         pattern = s[idx: idx + i] # s[0 : 3]
        #         new_idx = find_new_idx(idx, pattern) # find_new_idx(0, "abc")
        #         if (new_idx - idx) // len(pattern) == 1:
        #             dfs(new_idx, res + pattern)
        #         else:
        #             dfs(new_idx, res + str((new_idx - idx) // len(pattern)) + "[" + pattern + "]")
            
        # dfs(0, "")

        # return self.ans