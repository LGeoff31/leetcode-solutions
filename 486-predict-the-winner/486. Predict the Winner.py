class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        self.n = len(nums)
        def dfs(queue, one, two, turn): # true -> playerOne
            if not queue:
                print(one, two)
                return one >= two
            
            if turn:
                res = False
                # Take from the front
                val = queue.popleft()
                res = res or dfs(queue, one + val if turn else one, two + val if not turn else two, not turn)
                queue.appendleft(val)
                # Take from the back
                val = queue.pop()
                res = res or dfs(queue, one + val if turn else one, two + val if not turn else two, not turn)
                queue.append(val)
                return res
            else:
                res = True
                # Take from the front
                val = queue.popleft()
                res = res and dfs(queue, one + val if turn else one, two + val if not turn else two, not turn)
                queue.appendleft(val)
                # Take from the back
                val = queue.pop()
                res = res and dfs(queue, one + val if turn else one, two + val if not turn else two, not turn)
                queue.append(val)
                return res
    
        return dfs(deque(nums), 0, 0, True)
    
