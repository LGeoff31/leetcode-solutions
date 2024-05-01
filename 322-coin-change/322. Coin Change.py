from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins:
            return 1
        if amount == 0:
            return 0

        stage = 1
        queue = deque(coins) #[1,2,5]
        visited = set()

        def next_loc(num):
            lst = []
            for coin in coins:
                lst.append(num+coin) #[2,3,6]
            return lst

        while queue:
            for i in range(len(queue)):
                current_num = queue.popleft()
                for next_num in next_loc(current_num): #[2,3,6]
                    if next_num <= amount:
                        if next_num not in visited:
                            queue.append(next_num)
                            visited.add(next_num)
                        
            stage += 1
            if amount in queue:
                return stage
                

        return -1



        