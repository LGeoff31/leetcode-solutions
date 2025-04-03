class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        frequency = []
        for i, s in enumerate(stickers):
            frequency.append(defaultdict(int))
            for c in s:
                frequency[i][c] += 1
        cache = {}
        def dfs(target, sticker): # O (2^n * m)
            if target == "":
                return 0
            if target in cache:
                return cache[target]
            
            res = 1 if sticker else 0
            remain_target = ""
            # Try an exhaust sticker
            for c in target:
                if c in sticker and sticker[c] > 0:
                    sticker[c] -= 1
                else:
                    remain_target += c

            if remain_target:
                ans = 1e9
                for s in frequency:
                    if remain_target[0] in s:
                        ans = min(ans, dfs(remain_target, s.copy()))
                cache[remain_target] = ans
                res += ans
            return res

        return dfs(target, {}) if dfs(target, {}) != 1e9 else -1
