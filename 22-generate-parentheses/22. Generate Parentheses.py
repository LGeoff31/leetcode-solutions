from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque(["("])

        while queue:
            if len(queue[0]) == n * 2:
                break
            for i in range(len(queue)):
                curr = queue.popleft()
                number_open = curr.count("(")
                number_closed = curr.count(")")
                
                if number_open < n:
                    queue.append(curr + "(")
                if number_open > number_closed:
                    queue.append(curr + ")")



        # print(queue)
        return queue

        