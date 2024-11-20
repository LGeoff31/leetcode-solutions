class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        a,b,c = s.count("a"), s.count("b"), s.count("c")
        if k > min(a,b,c): return -1
        n = len(s)
        prefix=[]
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = 1 + dic.get(s[i], 0)
            prefix.append(dic.copy())
        suffix=[]
        dic = {}
        res = 1e9
        for i in range(len(s) - 1, -1, -1):
            dic[s[i]] = 1 + dic.get(s[i], 0)
            b = dic.copy()
            suffix.append(dic.copy())
            print("b", b)
            if b.get("a",0) >= k and b.get("b",0) >= k and b.get("c",0) >= k:
                res = min(res, n - i)
        suffix = suffix[::-1]
        n = len(s)
        # print("prefix", prefix, len(prefix))
        # print("suffix", suffix, len(suffix))
        for i in range(len(s)):
            # We have these characters
            
            need_a, need_b, need_c = max(0, k - prefix[i].get("a", 0)), max(0, k - prefix[i].get("b", 0)), max(0, k - prefix[i].get("c", 0))
            # print("need", need_a, need_b, need_c)
            if need_a == need_b == need_c == 0:
                res = min(res, i+1)
                continue
            # Now we need to binary search for the suffix index such that it satisfies the remainders
            local_res = 0
            l, r = i+1, len(s) - 1
            while l <= r:
                mid = (l + r) // 2
                if suffix[mid].get("a", 0) >= need_a and suffix[mid].get("b", 0) >= need_b and suffix[mid].get("c", 0) >= need_c:
                    # print('beep', mid, suffix[mid])
                    # Valid
                    local_res = max(local_res, mid)
                    l = mid + 1
                else:
                    r = mid - 1
                    
            res = min(res, i+1 + n-local_res)
            # print(res, i, local_res)
            # (i+1 -> 3) + (n - mid )
        return res

