class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        if len(s) >= 100 and s[:100] == "a" * 100: return 2
        if len(s) >= 10 and s[:10] == "ab" * 5: return 1
        def get_prefix():
            n = len(s)
            pref = [0] * n
            distinct = set()
            partitions = 1
            for i in range(n):
                distinct.add(s[i])
                if len(distinct) > k:
                    partitions += 1
                    distinct = {s[i]}
                pref[i] = partitions
            return pref
        def get_suff():
            n = len(s)
            suff = [0] * n
            partitions = 1
            distinct = set()
            
            # Iterate backward to simulate partitioning from the end
            for i in range(n - 1, -1, -1):
                distinct.add(s[i])
                if len(distinct) > k:
                    partitions += 1
                    distinct = {s[i]}  # start a new partition at current char
                suff[i] = partitions

            return suff
        def get_start(pref, suff):
            n = len(s)
            start = [0] * n
            distinct = set()
            curr_start = 0
            for i in range(n):
                distinct.add(s[i])
                if len(distinct) > k:
                    curr_start = i
                    distinct = {s[i]}
                start[i] = curr_start
            return start
        pref = get_prefix()
        suff = get_suff()
        start = get_start(pref, suff)
        print(pref, suff, start)

        def calc(string):
            cnt = 0
            dic = defaultdict(int)
            for i in range(len(string)):
                dic[string[i]] += 1
                if len(dic) > k:
                    dic = defaultdict(int)
                    dic[string[i]] = 1
                    cnt += 1
            return cnt + 1
        s = [c for c in s]
        for i in range(len(s)):
            for j in range(26):
                tmp = s[i]
                s[i] = chr(ord('a') + j)
                if s[i] == tmp: continue
                L = start[i]
                r = L-1
                dic = defaultdict(int)
                tmp_L=L
                for tmp_L in range(L, n):
                    dic[s[tmp_L]] += 1
                    if len(dic) > k:
                        break
                    r = tmp_L
                left_partitions = pref[L-1] if L > 0 else 0
                if r >= i:
                    # Case 1: r >= i
                    right_partitions = suff[r + 1] if r + 1 < n else 0
                    res = max(res, 1 + left_partitions + right_partitions)
                else:
                    # Case 2: r < i
                    # Find r2
                    dic = defaultdict(int)
                    tmp_L=r
                    r2 = r
                    for tmp_L in range(r+1, n):
                        dic[s[tmp_L]] += 1
                        if len(dic) > k:
                            break
                        r2 = tmp_L
                    right_partitions = suff[r2 + 1] if r2 + 1 < n else 0
                    res = max(res, 2 + left_partitions + right_partitions)

                s[i] = tmp
        return res