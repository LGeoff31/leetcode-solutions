class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dic = defaultdict(list)
        for i in range(len(ring)):
            dic[ring[i]].append(i) #increasing order binary search?
        #key is that you only have to go to closest right and left point
        # print(dic)
        @cache
        def dfs(center_idx, key_idx):
            if key_idx == len(key):
                return 0

            arr = dic[key[key_idx]]
            idx = bisect.bisect_left(arr, center_idx)
            go_left_idx = arr[(idx - 1) % len(arr)]
            go_right_idx = arr[idx % len(arr)]

            left_ans = dfs(go_left_idx, key_idx + 1) + min(abs(center_idx - go_left_idx), len(ring) - abs(center_idx - go_left_idx))
            right_ans = dfs(go_right_idx, key_idx + 1) + min(abs(center_idx - go_right_idx), len(ring) - abs(center_idx - go_right_idx))

            return min(left_ans, right_ans)

            
        return dfs(0, 0) + len(key)

