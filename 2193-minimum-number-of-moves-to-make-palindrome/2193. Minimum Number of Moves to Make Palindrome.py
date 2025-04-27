class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # Given at most 1 odd frequency character
        queue = deque(s)
        res = 0
        def find_last_idx(queue, num):
            for i in range(len(queue) - 1, -1, -1):
                if queue[i] == num:
                    return i
            return -1
        def get_new_queue(queue ,idx):
            new_queue = deque([])
            for i in range(len(queue)):
                if i != idx:
                    new_queue.append(queue[i])
            new_queue.append(queue[idx])
            return new_queue

        while len(queue) > 1:
            while len(queue) > 1 and queue[0] == queue[-1]:
                queue.popleft()
                queue.pop()
            if len(queue) <= 1: break
            idx = find_last_idx(queue, queue[0])
            if idx == 0:
                queue[0], queue[1] = queue[1], queue[0]
                res += 1
            else:
                queue = get_new_queue(queue, idx)
                res += len(queue) - idx - 1

            
            # queue[idx], queue[-1] = queue[-1], queue[idx]
            # print(queue, len(queue) - idx - 1)

        return res
            
            