class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        if "0000" in deadends: return -1
        deadends = set(deadends)
        moves = 0
        visited = set()
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target: return moves
                new1 = str((int(curr[0])+1) % 10) + curr[1] + curr[2] + curr[3]
                if new1 not in visited and new1 not in deadends:
                    visited.add(new1)
                    queue.append(new1)
                new2 = curr[0] + str((int(curr[1])+1) % 10) + curr[2] + curr[3]
                if new2 not in visited and new2 not in deadends:
                    visited.add(new2)
                    queue.append(new2)
                new3 = curr[0] + curr[1] + str((int(curr[2])+1) % 10) + curr[3]
                if new3 not in visited and new3 not in deadends:
                    visited.add(new3)
                    queue.append(new3)
                new4 = curr[0]   + curr[1] + curr[2] + str((int(curr[3])+1) % 10)
                if new4 not in visited and new4 not in deadends:
                    visited.add(new4)
                    queue.append(new4)
                #subtract
                new1 = str((int(curr[0])-1) % 10) + curr[1] + curr[2] + curr[3]
                if new1 not in visited and new1 not in deadends:
                    visited.add(new1)
                    queue.append(new1)
                new2 = curr[0] + str((int(curr[1])-1) % 10) + curr[2] + curr[3]
                if new2 not in visited and new2 not in deadends:
                    visited.add(new2)
                    queue.append(new2)
                new3 = curr[0] + curr[1] + str((int(curr[2])-1) % 10) + curr[3]
                if new3 not in visited and new3 not in deadends:
                    visited.add(new3)
                    queue.append(new3)
                new4 = curr[0]   + curr[1] + curr[2] + str((int(curr[3])-1) % 10)
                if new4 not in visited and new4 not in deadends:
                    visited.add(new4)
                    queue.append(new4)
            print(queue)
            moves+=1

        return -1
