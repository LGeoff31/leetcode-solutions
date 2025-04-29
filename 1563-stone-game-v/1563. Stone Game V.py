class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = [0] + list(accumulate(stoneValue)) 
        @cache
        def dfs(l, r):
            if l == r:
                return 0
                
            if all(stoneValue[k] == stoneValue[r] for k in range(l, r)):
                cnt = 0
                z = r - l + 1
                while z > 1:
                    z //= 2
                    cnt += z
                return cnt * stoneValue[r] 
                
            res = 0
            for split in range(l+1, r+1):
                leftSum = prefix[split] - prefix[l]
                rightSum = prefix[r + 1] - prefix[split]
                if leftSum < rightSum: res = max(res, leftSum + dfs(l, split - 1))
                elif leftSum > rightSum: res = max(res, rightSum + dfs(split, r))
                else: res = max(res, leftSum + dfs(l, split - 1), rightSum + dfs(split, r))
            return res
        
        return dfs(0, len(stoneValue) - 1)

        # res = 0
        # queue = deque([[0, len(stoneValue) - 1, 0]])
        # visited = {}
        # while queue:
        #     for i in range(len(queue)):
        #         left, right, score = queue.popleft()
        #         if (left, right) in visited and score < visited[(left, right)]:
        #             continue
        #         visited[(left, right)].add((left, right))
        #         if left == right:
        #             res = max(res, score)
        #             continue
        #         for split in range(left + 1, right + 1):
        #             # print('split', split)
        #             leftSum = prefix[split] - prefix[left]
        #             rightSum = prefix[right + 1] - prefix[split]
        #             if leftSum < rightSum:
        #                 queue.append([left, split - 1, leftSum + score])
        #             elif leftSum > rightSum:
        #                 queue.append([split, right, rightSum + score])
        #             else:
        #                 queue.append([left, split - 1, leftSum + score])
        #                 queue.append([split, right, rightSum + score])
        #     # print(queue)
            
        # return res