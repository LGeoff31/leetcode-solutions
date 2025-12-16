class Solution:
    def balancedString(self, s: str) -> int:
        """ 
        can determine which letters and of what quantity need to be added (LENGTH = 14)
        then derive an algorithm that will find those letters of that quantity -> SLIDING WINDOW??
        OR 
        Find a substring that has a length 14 that doesn't contain those letters
        """
        goal = len(s) // 4
        dic = Counter(s)
        total = 0
        bad_letters = set()
        for key in {"Q", "W", "E", "R"}:
            if key not in dic or dic[key] < goal:
                dic[key] = 0
                bad_letters.add(key)

            total += max(dic[key] - goal, 0)
        # print(total, bad_letters, len(s))
        l, r = 0, 0
        n = len(s)
        curr = 0
        res = 1e9
        window = defaultdict(int)
        while r < n:
            window[s[r]] += 1
            if s[r] not in bad_letters and dic[s[r]] - window[s[r]] >= goal:
                curr += 1
            if curr == total:
                res = min(res, r-l+1)
                # make it not valid anymore
                while curr == total and l < n:
                    if s[l] not in bad_letters and dic[s[l]] - window[s[l]] >= goal:
                        curr -= 1
                    res = min(res, r-l+1)
                    window[s[l]] -= 1
                    l += 1
            r += 1
            print(res)
        if curr == total:
            res = min(res, r-l+1)
        return res if res != 1e9 else 0