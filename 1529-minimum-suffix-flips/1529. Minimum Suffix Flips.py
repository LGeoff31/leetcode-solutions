class Solution:
    def minFlips(self, target: str) -> int:
        # Your first flip has to encompass the leftmost 1
        # Your second flip must toggle out the leftmost zero

        # Greedy algorithm

        def dfs(i, zeros):
            if i >= len(target):
                return 0
            print(i, zeros)
            if not zeros:
                # Find the first instance of a 0
                for idx in range(i, len(target)):
                    if target[idx] == "0":
                        return 1 + dfs(idx + 1, not zeros)
                return 0
            else:
                for idx in range(i, len(target)):
                    if target[idx] == "1":
                        return 1 + dfs(idx + 1, not zeros)
                return 0

        idx_one = len(target)
        for i in range(len(target)):
            if target[i] == "1":
                idx_one = i
                break 
        print(idx_one)
        return dfs(idx_one, True)
            
        