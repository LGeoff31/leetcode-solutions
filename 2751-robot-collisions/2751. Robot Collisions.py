class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        n = len(positions)
        indicies = list(range(n))
        indicies.sort(key=lambda x: positions[x])


        for idx in indicies:
            if directions[idx] == "R":
                stack.append(idx)
            else:
                while stack and healths[idx] > 0:
                    top = stack.pop()
                    if healths[top] > healths[idx]:
                        healths[top] -= 1
                        healths[idx] = 0
                        stack.append(top)
                    elif healths[top] < healths[idx]:
                        healths[idx] -= 1
                        healths[top] = 0
                    else:
                        healths[idx] = 0
                        healths[top] = 0
        # Suriving left sliders
        res = []
        for idx in range(n):
            if healths[idx] > 0:
                res.append(healths[idx])
        return res